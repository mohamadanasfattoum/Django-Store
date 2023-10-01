from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product



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

class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailAPI(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()