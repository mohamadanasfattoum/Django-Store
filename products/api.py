from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import ProductListSerializer, ProductDetailSerializer , BrandListSerializer,BrandDetailSerializer
from .models import Product, Brand
from .mypagination import MyPagination



'''
@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductSerializer(products,many=True,context ={'request':request}).data
    return Response({'products':data})

@api_view(['GET'])
def product_detail_api(request,product_id):
    product = Product.objects.get(id=product_id)
    data = ProductSerializer(product,context ={'request':request}).data
    return Response({'product':data})
'''

class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['flag', 'brand','price']
    ordering_fields = ['price']


class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()



class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()

class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()