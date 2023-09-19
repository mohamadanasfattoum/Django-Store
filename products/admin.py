from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Brand, ProductImages, Review


class ProductImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    inlines = [ProductImagesInline,]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)