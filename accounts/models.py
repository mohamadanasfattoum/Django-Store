from django.db import models
from utils.generate_code import generate_code
from django.contrib.auth.models import User 



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'accounts')
    code = models.CharField(max_length=10 , default= generate_code)
