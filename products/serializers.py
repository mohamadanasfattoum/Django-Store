from rest_framework import serializers
from .models import Product , Brand

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, source = 'product_brand')
    class Meta:
        model = Brand
        fields = '__all__'