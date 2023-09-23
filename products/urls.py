from django.urls import path
from .views import ProductList, ProductDetail, BrandList

urlpatterns = [
    path('' , ProductList.as_view()),
    path('<slug:slug>/', ProductDetail.as_view()),
    path('brand/' , BrandList.as_view()),
]