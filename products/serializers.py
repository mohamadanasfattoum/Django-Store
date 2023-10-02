from rest_framework import serializers
from .models import Product , Brand, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, source ='review_product')
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