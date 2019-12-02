from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls import url,include


urlpatterns = [
    #path('', views.home), 
    path('home/', LoginView.as_view(template_name='home.html'), name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LoginView.as_view(template_name='logout.html'), name="logout"),
  
   
    ]
