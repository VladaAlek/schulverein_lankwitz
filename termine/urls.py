from django.urls import path
from .views import termine

urlpatterns = [
    path('', termine, name='termine')
]
