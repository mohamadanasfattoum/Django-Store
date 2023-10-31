from rest_framework import serializers
from .models import Cart, Order, CartDetail, OrderDetail, Coupon






class CartSerializer(serializers.ModelSerializer):

    class Meta:
        Model=Cart
        fields='__all__'