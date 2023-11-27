from django.db import models
from utils.generate_code import generate_code
from django.contrib.auth.models import User 

from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'accounts')
    code = models.CharField(max_length=10 , default= generate_code)



@receiver(post_save,sender=User) # لم اليوسر ينعمله تسجيل جديد ويتسيف  بتناده عليها
def create_profile(sender,instance,created,**kwargs): # مين ارسل الاشارةsender. instance المستخدم.  ceared  هل المستخدم نشأ ولالأ
    if created:# if true لسى عامل الحساب  or fulse   اليوسر يعمل تعديل
        Profile.objects.get(
            user= instance


        )




NUMBER_TYPS = (
    ('Primary','Primary') ,
    ('Secondary','Secondary')
     )


class ContactNumbers(models.Model):
    user = models.ForeignKey(User, related_name='user_phones', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=NUMBER_TYPS)
    number = models.CharField(max_length=10)


ADDRESS_TYPS = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussiness','Bussiness'),
    ('Academy','Academy'),
    ('Others','Others')
)


class Address(models.Model):
    user = models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=ADDRESS_TYPS)
    address = models.CharField(max_length=150)