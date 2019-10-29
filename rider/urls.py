from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^rhome/', views.rhome),
    url(r'^rprofile/', views.rprofile),
    url(r'^changepassword/', views.changepassword),
    url(r'^setpassword/', views.setpassword),
    url(r'^rshowhistory/', views.rshowhistory),
    url(r'^current/', views.current),
    url(r'^remove/', views.remove),
]