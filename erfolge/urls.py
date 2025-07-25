from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.erfolge_view, name= "erfolge")
]