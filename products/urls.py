from django.urls import path
from .views import ProductList, ProductDetail, BrandtList, BrandtDetail

urlpatterns = [
    path('', ProductList.as_view()),
    path('<slug:slug>/', ProductDetail.as_view()),
    path('brand/' , BrandtList.as_view()),
]