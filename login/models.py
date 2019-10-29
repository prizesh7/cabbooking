from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime  

# Create your models here.


class Otp(models.Model):
	uname= models.CharField(max_length=100, blank=True)
	otp = models.CharField(max_length=100, blank=True)