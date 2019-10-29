from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import Rider,Driver,Availabledriver
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from passlib.hash import oracle10


def addriderinfo(request):
	fname = request.POST.get('firstname', '')
	lname = request.POST.get('lastname', '')
	ph_no=request.POST.get('phone','')
	email= request.POST.get('email', '')
	city=request.POST.get('pass', '')
	uname = request.POST.get('uname', '')
	password = request.POST.get('pass', '')
	#p=oracle10.hash(password,user=uname)
	#print(fname,lname,ph_no,email,uname,p)
	user = auth.authenticate(username=uname, password=password)
	if user is None:
		user=User.objects.create_user(uname,email,password)
		user.save()
		s = Rider(username=uname,fname=fname,lname=lname,phone_no=ph_no,email=email,city=city)
		s.save()
		user = auth.authenticate(username=uname, password=password)
		auth.login(request, user)
		return HttpResponseRedirect('/rider/rhome/')
	else:
		return render(request,'rider.html')
def adddriverinfo(request):
	print(request.POST.get('firstname', ''))
	fname = request.POST.get('firstname', '')
	lname = request.POST.get('lastname', '')
	ph_no=request.POST.get('phone','')
	email= request.POST.get('email', '')
	city= request.POST.get('city', '')
	uname = request.POST.get('uname', '')
	password = request.POST.get('pass', '')
	#p=oracle10.hash(password,user=uname)
	#print(fname,lname,ph_no,email,city,uname,p)
	user = auth.authenticate(username=uname, password=password)
	if user is None:
		user=User.objects.create_user(uname,email,password)
		user.save()
		s = Driver(username=uname,fname=fname,lname=lname,phone_no=ph_no,email=email,city=city)
		s.save()
		s1=Availabledriver(username=uname,fname=fname,lname=lname,phone_no=ph_no)
		s1.save()
		user = auth.authenticate(username=uname, password=password)
		auth.login(request, user)
		return HttpResponseRedirect('/driver/dhome/')
	else:
		return render(request,'driver.html')

def select(request):
	return render(request,'select.html')

def riderform(request):
	return render(request,'rider.html')

def driverform(request):
	return render(request,'driver.html')