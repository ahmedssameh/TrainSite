from django.urls import path
from . import views
from user import views as user_view
from django.conf.urls import url

app_name = 'Wallet'

urlpatterns =[
     path('info', views.register, name="register"),
     path('Payment', views.log, name="login")
]