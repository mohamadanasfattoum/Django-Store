from rest_framework import serializers
from .models import Product , Brand

class ProductSerializer(serializers.ModelSerializer):
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_reviews_count(self,object):
        reviews_count= object.review_product.all().count()
        return reviews_count


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, source = 'product_brand')
    class Meta:
        model = Brand
        fields = '__all__'