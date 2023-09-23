from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product , ProductImages

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["product-image"] = ProductImages.objects.filter(Product=self.get_object())
        return context