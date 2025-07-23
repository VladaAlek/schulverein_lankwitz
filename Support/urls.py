from django.urls import path
from .views import support_home

urlpatterns = [
    path('', support_home, name='support_home'),
]