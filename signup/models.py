from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Rider(models.Model):
	username= models.CharField(max_length=100, primary_key=True)
	fname = models.CharField(max_length=100, blank=True)
	lname= models.CharField(max_length=100, blank=True)
	phone_no= models.CharField(max_length=10, blank=True)
	email= models.CharField(max_length=100, blank=True)
	city= models.CharField(max_length=25, blank=True)
	#password= models.CharField(max_length=50, blank=True)

class Driver(models.Model):
	username= models.CharField(max_length=100, primary_key=True)
	fname = models.CharField(max_length=100, blank=True)
	lname= models.CharField(max_length=100, blank=True)
	phone_no= models.CharField(max_length=10, blank=True)
	email= models.CharField(max_length=100, blank=True)
	city= models.CharField(max_length=25, blank=True)
	#password= models.CharField(max_length=50, blank=True)

class Availabledriver(models.Model):
	username= models.CharField(max_length=100, primary_key=True)
	fname = models.CharField(max_length=100, blank=True)
	lname= models.CharField(max_length=100, blank=True)
	phone_no= models.CharField(max_length=10, blank=True)
