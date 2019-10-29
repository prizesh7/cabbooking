from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^authriderinfo/', views.authriderinfo),
    url(r'^authdriverinfo/', views.authdriverinfo),
    url(r'^select1/', views.select1),
    url(r'^riderlogin/', views.riderlogin),
    url(r'^logout/', views.logout),
    url(r'^driverlogin/', views.driverlogin),
    url(r'^forgot/', views.forgot),
    url(r'^forgotsend/', views.forgotsend),
    url(r'^newpass/', views.newpass),
]