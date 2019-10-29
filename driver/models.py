from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime  
# Create your models here.

'''class Ride_history(models.Model):
	uname = models.CharField(max_length=100, blank=True)
	fname = models.CharField(max_length=100, blank=True)
	lname= models.CharField(max_length=100, blank=True)
	phone_no= models.CharField(max_length=10, blank=True)
	pickup= models.CharField(max_length=100, blank=True)
	drop= models.CharField(max_length=50, blank=True)
	date = models.DateTimeField(default=datetime.now(), blank=True)'''