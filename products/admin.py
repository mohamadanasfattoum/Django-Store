from django.contrib import admin
from .models import Product, Brand, ProductImages, Review

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)