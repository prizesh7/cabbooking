from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^sendemail/', views.sendemail),
    url(r'^info_cansle/', views.info_cansle),
]