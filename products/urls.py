from django.urls import path
from .views import ProductList, ProductDetail, BrandList ,BrandDetail
from .api import product_list_api ,product_detail_api, ProductListAPI



urlpatterns = [
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetail.as_view()),
    


    path('api/list', ProductListAPI.as_view()),
    path('api/list/<int:product_id>', product_detail_api),
]