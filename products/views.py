from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product , ProductImages, Review, Brand
from django.db.models import Q , F , Value

def mydebug(request):
    # data = Product.objects.all() 
    # data = Product.objects.filter(price__gt= 90) # >90
    # data = Product.objects.filter(price__gte= 90) # >=90
    # data = Product.objects.filter(price__lt = 22) # <22
    # data = Product.objects.filter(price__lte = 22) # <=22
    # data = Product.objects.filter(price__range = (90,91)) # range  


    # data = Product.objects.filter(name__contains='ian') # name
    # data = Product.objects.filter(name__startswith='ian') # start name
    # data = Product.objects.filter(name__endswith='ia') # name end
    # data = Product.objects.filter(name__isnull=True) # without name

    # data = Product.objects.filter(price__gt= 90 , name__startswith='ian') #لأسخدام فلترين بشرط تواجد الشرطبن

    # data = Product.objects.filter(
    # Q(price__gt= 90) &
    # Q(name__startswith='ian')
    # ) # and &

    
    # data = Product.objects.filter(
    #     Q(price__gt= 90) |
    #     Q(name__startswith='ian')
    #     ) #  or |


    # data = Product.objects.filter(
    #     Q(price__gt= 90) |
    #     ~Q(name__startswith='ian')
    #     ) # not اي اسم اكبر من الرقم وليس الاسم هذا

    # data = Product.objects.filter(quantity = F('price')) # للفلترة بجدولين.متساويين

    # data = Product.objects.all().order_by('price') # ordnen mit price
    # data = Product.objects.order_by('price')
    # data = Product.objects.order_by('-price') # DESC تنازلي 
    # data = Product.objects.order_by('price').reverse()   # DESC تنازلي 
    # data = Product.objects.order_by('price' , 'name') # ranking ترتيب بجدولين
    # data = Product.objects.filter(price__gt= 90).order_by('-price') # with filter and desc

    # data = Product.objects.order_by('price')[:8] # first 8
    # data = Product.objects.order_by('price')[0] # the first one
    # data = Product.objects.earliest('price') # the first one
    # data = Product.objects.latest('price') # the last one

    # data = Product.objects.values('name','price')   # just 'name','price' 2 values
    # data = Product.objects.only('name','price') #  في هذه الحالة لاتضف كويري داتا اضافية وغير معرفة في التمبلت اضف فقط الكويري الراجعة من الفيو متل الاسم وسعر
    # data = Product.objects.defer('vidio_url','description') # without 'vidio_url','description'

    # data = Product.objects.select_related('brand').all() # ForeignKey and one-to-one
    # data = Product.objects.prefetch_related('brand').all() # many-to-many
    # sarch about django queryset api Documentation


    data = Product.objects.all() 

    return render (request, 'products/debug.html', {'data':data})


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