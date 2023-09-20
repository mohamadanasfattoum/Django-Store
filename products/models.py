from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify

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
    quantity = models.IntegerField()
    tags = TaggableManager()
    vidio_url = models.URLField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name= 'product_image')
    image = models.ImageField(upload_to='product_images')




class Brand(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='brand')

    def __str__(self) -> str:
        return self.name



class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user', on_delete=models.SET_NULL,null=True , blank= True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name= 'review_product')
    review = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default= timezone.now)
    rate = models.IntegerField()


    def __str__(self) -> str:
        return str(self.product)