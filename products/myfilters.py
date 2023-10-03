from django_filters import rest_framework as filters
from .models import Product
import django_filters

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'price' : ['range']
        }