from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
	url(r'^login/', views.login),
    url(r'^validateadmin/', views.validateadmin),
	url(r'^viewdriver/', views.viewdriver),
    

]