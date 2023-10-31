from rest_framework import generics
from rest_framework.response import responses
from .serializers import CartSerializer, OrderSerializer, CartDetailSerializer, OrderDetailSerializer
from products.models import Product, Brand
from django.contrib.auth.models import User
from .models import Cart, CartDetail, Order, OrderDetail, Coupon


class CartDetailCreateDeleteAPI(generics.GenericAPIView):
    pass