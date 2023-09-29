from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product , ProductImages, Review, Brand

class ProductList(ListView):
    model = Product
    paginate_by = 30


class ProductDetail(DetailView):
    model = Product


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImages.objects.filter(product=self.get_object())
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context
    


class BrandList(ListView):
    model = Brand
    paginate_by = 10



#class BrandDetail(DetailView):
#    model = Brand


class BrandDetail(ListView): #change
    model = Product
    template_name = 'products/brand_detail.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(BrandDetail , self).get_queryset()
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = queryset.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context