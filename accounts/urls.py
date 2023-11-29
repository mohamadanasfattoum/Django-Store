from django.urls import path
from .views import signup, activate

app_name = 'accounts'

urlpatterns = [
    path('signup', signup),
    path('<str:username>/activate', activate),
]