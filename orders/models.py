from django.db import models
from django.contrib.auth.models import User


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
    



class OrderDetail(models.Model):
    pass
