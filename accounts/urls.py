from django.urls import path
from .views import signup, activate, dashboard

app_name = 'accounts'

urlpatterns = [
    path('signup', signup),
    path('dashboard', dashboard),    
    path('<str:username>/activate', activate),
]