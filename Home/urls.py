from django.urls import path
from . import views

urlpatterns = [
    path('mainpage', views.Home, name='Home'),
    path('info',views.Info,name='Info')
]

#http://127.0.0.1:8000/home/info