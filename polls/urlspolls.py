from django.contrib import admin
from . import views
from django.urls import path
from django.conf.urls import url,include


urlpatterns = [
    #path('', views.home), 
    path('vote/', LoginView.as_view(template_name='vote.html'), name="vote"),
    path('uservote/', LoginView.as_view(template_name='uservote.html'), name="vote"),
    #path('logout/', LoginView.as_view(template_name='logout.html'), name="logout"),
  
   
    ]