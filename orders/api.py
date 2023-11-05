from rest_framework import generics
from rest_framework.response import Response

from .serializers import CartSerializer, OrderListSerializer, OrderDetailSerializer
from products.models import Product, Brand
from django.contrib.auth.models import User
from .models import Cart, CartDetail, Order, OrderDetail, Coupon


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
    pass




class CreateOrderAPI(generics.GenericAPIView):
    pass





class ApplyCouponAPI(generics.GenericAPIView):
    pass
