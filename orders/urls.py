from django.urls import path
from .views import order_list, checkout, add_to_cart
from .api import CartDetailCreateDeleteAPI, OrderListAPI, OrderDetailAPI, CreateOrderAPI, ApplyCouponAPI

urlpatterns= [
    path('' , order_list),
    path('add-to-cart', add_to_cart),
    path('checkout' , checkout),



    #api
    path('api/<str:username>/list', OrderListAPI.as_view()),
    path('api/<str:username>/order/create', CreateOrderAPI.as_view()),    
    path('api/<str:username>/list/<int:pk>', OrderDetailAPI.as_view()),
    path('api/<str:username>/cart', CartDetailCreateDeleteAPI.as_view()),
    path('api/<str:username>/cart/apply-coupon', ApplyCouponAPI.as_view()),







]