from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^searchcab/', views.searchcab),
    url(r'^confirm/', views.confirm),
    url(r'^verify/', views.verify),
    url(r'^endtrip/', views.endtrip),
]