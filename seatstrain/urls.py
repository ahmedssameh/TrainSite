from django.urls import path
from . import views
from user import views as user_view
from django.conf.urls import url

app_name='seatstrain'

urlpatterns =[
    path('seats', views.seats, name='seats'),
    path('seat', views.seat, name='seat'),
    path('<int:id>', views.Update, name='Update')

]
