from rest_framework import generics
from rest_framework.response import Response
from .serializers import CartSerializer, OrderSerializer, CartDetailSerializer, OrderDetailSerializer
from products.models import Product, Brand
from django.contrib.auth.models import User
from .models import Cart, CartDetail, Order, OrderDetail, Coupon


class CartDetailCreateDeleteAPI(generics.GenericAPIView): # كلاس فارغة استطيع ان اخصص بها ما اشاء GenericAPIViewباستخدام
    def get(self,request,*args,**kwargs):# دالة لاحضار الليس ويتيل
        
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,status='inprogress')
        data = CartDetailSerializer(cart).data #??
        return Response({'Cart':data})


    #def post(): # دالة لحتى اضيف
        #pass


    #def delete():
        #pass 

    pass