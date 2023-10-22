from django.shortcuts import render
from .models import Order, OrderDetail, Cart,CartDetail, Coupon


def order_list(request):
    order= Order.objects.all()
    return render(request,'orders/orders.html',{'order':order})


