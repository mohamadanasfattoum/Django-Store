from django.urls import path
from .views import singup, activate

app_name = 'accounts'

urlpatterns = [
    path('singup', singup),
    path('<str:username>/activate', activate),
]