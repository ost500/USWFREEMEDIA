from django.conf.urls import url
from django.contrib import admin
from Forum import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name = 'home'),
    url(r'^test/$', views.examples),
    
]
