from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import Rider,Driver
from login.models import Otp
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from passlib.hash import oracle10
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.utils.crypto import get_random_string
import smtplib

def home(request):
	return render(request,'home.html')

def select1(request):
	return render(request,'select1.html')

def riderlogin(request):
	return render(request,'loginrider.html')

def driverlogin(request):
	return render(request,'logindriver.html')

def authriderinfo(request):
	uname = request.POST.get('uname', '')
	password = request.POST.get('pass', '')
	user = auth.authenticate(username=uname, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/rider/rhome/')
	else:
		messages.add_message(request,messages.WARNING,'Incorrect Username or password')
		return render(request,'loginrider.html')

def authdriverinfo(request):
	uname = request.POST.get('uname', '')
	password = request.POST.get('pass', '')
	user = auth.authenticate(username=uname, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/driver/dhome/')
	else:
		messages.add_message(request,messages.WARNING,'Incorrect Username or password')
		return render(request,'logindriver.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/home/home/')

def forgot(request):
	return render(request,'forgot.html')

def forgotsend(request):
	uname = request.POST.get('uname', '')
	l=Rider.objects.filter(username=uname)
	l=list(l.values())
	if(len(l)>0):
		l=l[0]
		otp = get_random_string(6, allowed_chars='0123456789')
		s=Otp(uname=uname,otp=otp)
		server=smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.login("prizeshbhadaniya@gmail.com","prizesh345")
		uname = request.user.username
		email=l['email']
		msg='To:'+ email+'\n'+'From:prizeshbhadaniya@gmail.com'+'\n'+'Subject:otp\n'
		msg=msg + "hello  " +uname+'\n'+ "your verify otp is  " +otp
		server.sendmail("prizeshbhadaniya@gmail.com",email,msg)
		return render(request,'getotp.html')
	else:
		messages.add_message(request,messages.WARNING,'No user Exist')
		return render(request,'getotp.html')


def newpass(request):
	otp = request.POST.get('otp', '')
	pass1=request.POST.get('pass', '')
	l=Rider.objects.filter(username=uname)
	l=list(l.values())
	l=l[0]
	if(l['otp']==otp):
		s = User.objects.get(username__exact=uname)
		s.set_password(password)
		s.save()
	else:
		messages.add_message(request,messages.WARNING,'Incorrect OTP')
		return render(request,'getotp.html')


