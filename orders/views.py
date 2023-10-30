from django.shortcuts import render
from .models import Order, OrderDetail, Cart, CartDetail, Coupon
from settings.models import DeliveryFee

def order_list(request):
    orders= Order.objects.all()
    return render(request,'orders/orders.html',{'orders':orders})


def checkout(request):
    cart = Cart.objects.get(user=request.user,status='inprogress')
    cart_detail= CartDetail.objects.filter(cart=cart)
    delivery_fee= DeliveryFee.objects.last().fee
    sub_total = cart.cart_total()
    total = sub_total + delivery_fee
    discount= 0

    return render(request,'orders/checkout.html',{
        'cart':cart ,
        'cart_detail':cart_detail,
        'delivery_fee' : delivery_fee,
        'sub_total' : sub_total,
        'total' : total,
        'discount': discount,

    })