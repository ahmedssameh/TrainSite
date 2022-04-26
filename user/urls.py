from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth
from user import views as user_view



urlpatterns =[
#path('login/', views.Login, name ='login'),
#path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
#path('SignUp/', views.register, name ='register'),
#path('Update/',user_view.Update,name="Update" ),
#path('', views.index, name='index'),

    path('', views.index, name='index'),


]