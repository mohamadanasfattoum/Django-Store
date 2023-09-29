from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


def product_list_api(request):
    product = Product.objects.all()
    data = ProductSerializer(Product, many=True).data