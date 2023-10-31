from rest_framework import generics
from rest_framework.response import Response
from .serializers import CartSerializer, OrderSerializer
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



    def delete(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username']) #بحاجة مسح عنصر لالداخل وليس كل الكارت
        product= Product.objects.get(id=request.Post['product_id'])
        cart = Cart.objects.get(user=user,status='inprogress')
    

        cart_detail = CartDetail.objects.get(cart=cart, product=product)
        cart_detail.detete()
        return Response('message':'product was deteted successfuly')