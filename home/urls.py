from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^home/', views.home),
    url(r'^about/', views.about),
	url(r'^news/', views.news),
	url(r'^contact/', views.contact),
	url(r'^citytaxi/', views.citytaxi),
	url(r'^rental/', views.rental),
	url(r'^outstation/', views.outstation),
	url(r'',views.home),
]