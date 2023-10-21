from collections.abc import Iterable
from typing import Any
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone
import datetime
from utils.generate_code import generate_code

ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)



class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_owner' , on_delete= models.SET_NULL , null=True, blank=True)
    # user >> ForeignKey >> set_null لأن اذا المستخدم سكر حسابه وكان طالب اوردرات لازم تبقى لأن صاحب الموقع بحاجتها   
    # بس بحال cas بتنحذف بيانات الوردر مع اغلاق العمبل لحسابه
    # ForeignKey لان علاقة العديد لواحد زبون واحد يطلب عدة اوردرات

    status = models.CharField(max_length=12, choices=ORDER_STATUS, default='Recieved')
    code = models.CharField(max_length=10, default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)
    coupon = models.ForeignKey('Coupon', related_name='order_coupon', on_delete=models.SET_NULL, null=True, blank=True)
    order_total_discount= models.FloatField(null=True, blank=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_delait', on_delete=models.CASCADE)
    # order >> ForeignKey (Order)=(OrderDetail1+OrderDetail2+OrderDetail3)لأن داخل الاودر يوجد كذا اوردر دتيل
    product = models.ForeignKey(Product, related_name='orderdetail_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()



CART_STATUS = (
    ('inprogress','inprogress'),
    ('completed','completed'),
)


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_owner' , on_delete= models.SET_NULL , null=True, blank=True)
    status = models.CharField(max_length=12, choices=CART_STATUS, default='inprogress')
    coupon = models.ForeignKey('Coupon', related_name='cart_coupon', on_delete=models.SET_NULL, null=True, blank=True)
    order_total_discount= models.FloatField(null=True, blank=True)


class CartDetail(models.Model):
    Cart = models.ForeignKey(Order, related_name='cart_delait', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cartdetail_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    total = models.FloatField()



class Coupon(models.Model):
    code = models.CharField(max_length=12)
    start_date = models.DateField(default=timezone.now)

    end_date = models.DateField(null=True, blank=True) # بستخدام دالة السييف يمكن تحديد المدة عن طريق الداتا ديلتا وحفظها

    quantity = models.IntegerField()
    discount = models.FloatField()

    def save(self, *args, **kwargs):
        week = datetime.timedelta(days=7)
        self.end_date= self.start_date + week
        super(Coupon, self).save(*args, **kwargs)

