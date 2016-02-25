from django.conf.urls import url
from django.contrib import admin
from Forum import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name = 'home'),
    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    url(r'^category/(\d+)/$', views.EachCateView.as_view(), name='eachcate'),
    url(r'^new/$', views.NewView.as_view(), name='new'),
    url(r'^(\d+)/$', views.ArticleView.as_view(), name='detail')
       
]
