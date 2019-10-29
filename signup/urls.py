from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^addriderinfo/', views.addriderinfo),
    url(r'^adddriverinfo/', views.adddriverinfo),
    url(r'^select/', views.select),
    url(r'^riderform/', views.riderform),
    url(r'^driverform/', views.driverform),
]