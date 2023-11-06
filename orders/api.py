from rest_framework import generics
from rest_framework.response import Response

from .serializers import CartSerializer, OrderListSerializer, OrderDetailSerializer
from products.models import Product, Brand
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Cart, CartDetail, Order, OrderDetail, Coupon
import datetime
from settings.models import DeliveryFee

class CartDetailCreateDeleteAPI(generics.GenericAPIView): # كلاس فارغة استطيع ان اخصص بها ما اشاء GenericAPIViewباستخدام
    serializer_class= CartSerializer
    
    def get(self,request,*args,**kwargs):# دالة لاحضار الليس ويتيل
        
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,status='inprogress')
        data = CartSerializer(cart).data #??
        return Response({'Cart':data})


    def post(self,request,*args,**kwargs):  # دالة لحتى اضيف
        user = User.objects.get(username=self.kwargs['username'])
        product= Product.objects.get(id=request.Post['product_id'])
        quantity= int(request.POST['quantity'])


        cart = Cart.objects.get(user=user,status='inprogress')
        cart_detail, created = CartDetail.objects.get_or_create(cart=cart, product=product)
        cart_detail.price= product.price
        cart_detail.quantity = quantity
        cart_detail.total = round(quantity*product.price,2)
        cart_detail.save()

        return Response({'message':'product was added successfuly'})



    def delete(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username']) #بحاجة مسح عنصر لالداخل وليس كل الكارت
        product= Product.objects.get(id=request.Post['product_id'])
        cart = Cart.objects.get(user=user,status='inprogress')
    

        cart_detail = CartDetail.objects.get(cart=cart, product=product)
        cart_detail.detete()

        return Response({'message':'product was deteted successfuly'})
    

class OrderListAPI(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def list(self, request, *args, **kwargs): #لحتى يرجع فقط باليس تبع الاوردر المطلوب
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        data = OrderListSerializer(queryset,many=True).data
        return Response(data)



class OrderDetailAPI(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer



class CreateOrderAPI(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,status='inprogress')
        cart_detail= CartDetail.objects.filter(cart=cart)



        # cart-------------> order
        new_order = Order.objects.create(
            user = user ,
            coupon = cart.coupon,
            order_total_discount = cart.order_total_discount
            
        )
        # cart_detail-------------> order_detail
        for object in cart_detail:
            OrderDetail.objects.creat(
                order = new_order ,
                product = object.product,
                quantity = object.quantity,
                price = object.product.price ,
                total = object.total
            )
        cart.status= 'completed'
        cart.save({'messege':'Your Order Was Created Successfully'})
            


class ApplyCouponAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,status='inprogress')
        coupon = get_object_or_404(Coupon , code=request.data['coupon_code'])    #لكي لايتوقف الموقع عند هدم تطابق الكود


        if coupon and coupon.quantity > 0 :  # للتأكد من الوقت 
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = sub_total / 100*coupon.discount
                sub_total = sub_total - coupon_value
                

                cart.coupon = coupon
                cart.order_total_discount = sub_total # مجموع الخقم الرئيسي
                coupon.quantity -= 1
                cart.save()
                coupon.save()
                return Response ({'messege':'coupon was applied successfully'})           
            return Response ({'messege':'coupon is not working'})
        return Response ({'messege':'coupon is not valid'})




