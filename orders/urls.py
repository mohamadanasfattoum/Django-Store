from django.urls import path
from .views import order_list, checkout
from .api import CartDetailCreateDeleteAPI, OrderListAPI, OrderDetailAPI, ApplyCouponAPI

urlpatterns= [
    path('' , order_list),
    path('checkout' , checkout),



    #api
    path('api/<str:username>/list', OrderListAPI.as_view()),
    path('api/<str:username>/cart', CartDetailCreateDeleteAPI.as_view()),







]