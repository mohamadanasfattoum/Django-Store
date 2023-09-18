from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

FLAG_CHOICES = (
    ('Sale','Sale'),
    ('Feature','Feature'),
    ('New','New'),
)

class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='peoduct')
    price = models.FloatField()
    flag = models.CharField(max_length=10, choices=FLAG_CHOICES)
    brand = models.ForeignKey('Brand', related_name='product_brand', on_delete=models.SET_NULL, null=True, blank=True )
    sku = models.CharField(max_length=10)
    subtitle = models.CharField(max_length=500)
    description = models.TextField(max_length=50000)
    tags = TaggableManager()
    vidio_url = models.URLField()
    slug = models.SlugField(null=True, blank=True)




class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name= 'product_image')
    image = models.ImageField(upload_to='product_images')




class Brand(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='brand')





class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user', on_delete=models.SET_NULL,null=True , blank= True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name= 'review_product')
    review = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default= timezone.now)
    rate = models.IntegerField()
