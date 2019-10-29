from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime  

# Create your models here.

class Cabdriver(models.Model):
	username= models.CharField(max_length=100, primary_key=True)
	otp = models.CharField(max_length=100, blank=True)
	pickup= models.CharField(max_length=100, blank=True)
	drop = models.CharField(max_length=100, blank=True)

class History(models.Model):
	r_uname= models.CharField(max_length=100, blank=True)
	d_uname= models.CharField(max_length=100, blank=True)
	pickup= models.CharField(max_length=100, blank=True)
	drop= models.CharField(max_length=100, blank=True)
	date = models.DateTimeField(default=datetime.now(), blank=True)

class Current(models.Model):
	r_uname= models.CharField(max_length=100, blank=True)
	d_uname= models.CharField(max_length=100, blank=True)
	pickup= models.CharField(max_length=100, blank=True)
	drop= models.CharField(max_length=100, blank=True)
	otp = models.CharField(max_length=100, blank=True)