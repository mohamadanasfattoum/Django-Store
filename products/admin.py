from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Brand, ProductImages, Review

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)