from django.urls import path
from .views import order_list, checkout
from .api import CartDetailCreateDeleteAPI

urlpatterns= [
    path('' , order_list),
    path('checkout' , checkout),



    #api
    path('api/<str:username>/cart', CartDetailCreateDeleteAPI.as_view()),
]