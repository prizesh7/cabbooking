from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^dhome/', views.dhome),
    url(r'^dprofile/', views.dprofile),
    url(r'^dshowhistory/', views.dshowhistory),
]