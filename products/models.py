from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='peoduct')
    price = models.FloatField()






class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name= 'product_image')
    image = models.ImageField(upload_to='product_images')