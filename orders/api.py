from rest_framework import generics
from rest_framework.response import responses
from .serializers import CartSerializer, OrderSerializer, CartDetailSerializer, OrderDetailSerializer
from products.models import Product, Brand
from django.contrib.auth.models import User
from .models import Cart, CartDetail, Order, OrderDetail, Coupon


class CartDetailCreateDeleteAPI(generics.GenericAPIView): # كلاس فارغة استطيع ان اخصص بها ما اشاء GenericAPIViewباستخدام
    def get():# دالة لاحضار الليس ويتيل
        pass


    def post(): # دالة لحتى اضيف
        pass


    def delete():
        pass 