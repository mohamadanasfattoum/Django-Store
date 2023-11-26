from django.db import models
from utils.generate_code import generate_code
from django.contrib.auth.models import User 



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'accounts')
    code = models.CharField(max_length=10 , default= generate_code)


NUMBER_TYPS = (
    ('Primary','Primary') ,
    ('Secondary','Secondary')
     )


class ContactNumbers(models.Model):
    user = models.ForeignKey(User, related_name='user_phones', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=NUMBER_TYPS)
    number = models.CharField(max_length=10)


class Address(models.Model):
    pass