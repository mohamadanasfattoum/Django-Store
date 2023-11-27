from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm): # لتشفير الكود
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ActivationForm(forms.Form): #لاستلتم الكود لزون تخزينه
    code = forms.CharField(max_length=10)
