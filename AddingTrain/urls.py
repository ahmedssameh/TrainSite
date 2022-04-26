from django.urls import path
from . import views

urlpatterns = [
    path('trains', views.trains, name='AddingTrain')

]
