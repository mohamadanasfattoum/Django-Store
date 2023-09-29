from django.shortcuts import render
from products.models import Product, Brand, Review


def home(request):
    brands = Brand.objects.all()[:20]
    sale_products = Product.objects.filter(flag='Sale')[:10]
    featur_products = Product.objects.filter(flag='Feature')[:6]



    return render(request,'settings/home.html',{
        'brands':brands, 'sale_products':sale_products, 'featur_products':featur_products
        })
