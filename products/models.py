from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='peoduct')
    price = models.FloatField()






class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name= 'product_image')
    image = models.ImageField(upload_to='product_images')


class ProductReviews(models.Model):
    user = models.ForeignKey(User,related_name='review_user', on_delete=models.SET_NULL,null=True , blank= True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name= 'review_product')
    review = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default= timezone.now)
    rate = models.IntegerField()