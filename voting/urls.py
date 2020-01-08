"""voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views
from polls import viewspolls
from voting import views as voting_views   
urlpatterns = [
    path('',voting_views.loginredirect,name='login redirect'),
    path('admin/', admin.site.urls),
    path('', include('login.urlslogin')),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.editprofile,name='editprofile'),
    path('vote/',viewspolls.vote,name='vote'),
    path('uservote/',viewspolls.uservote,name='uservote'),


]

