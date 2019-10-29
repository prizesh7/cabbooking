from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import Rider,Driver
from cabsearch.models import History,Current
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from passlib.hash import oracle10
from django.contrib.auth.models import User,Group
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import auth

@login_required(login_url = '/login/riderlogin/')
def rhome(request):
	return render(request,'rhome.html')

@login_required(login_url = '/login/riderlogin/')
def rprofile(request):
	uname=request.user.username
	l=Rider.objects.filter(username=uname)
	l=list(l.values())
	d=l[0]
	return render(request,'rprofile.html',{'d':d})

@login_required(login_url = '/login/riderlogin/')
def changepassword(request):
	return render(request,'password.html')

@login_required(login_url = '/login/riderlogin/')
def setpassword(request):
	old = request.POST.get('old', '')
	password = request.POST.get('pass', '')
	uname=request.user.username
	user = auth.authenticate(username=uname, password=old)
	print(user)
	if user is not None:
		s = User.objects.get(username__exact=uname)
		s.set_password(password)
		s.save()
		#return render(request,'rhome.html')
		return HttpResponseRedirect('/login/logout/')
	else:
		return render(request,'password.html')

def rshowhistory(request):
	uname=request.user.username
	s=History.objects.filter(r_uname=uname)
	d=list(s.values())
	a=[]
	for x in d:
		d1=Driver.objects.filter(username=x['d_uname'])
		d1=list(d1.values())
		d1=d1[0]
		d1.update({'pickup':x['pickup']})
		d1.update({'drop':x['drop']})
		a.append(d1)
	return render(request,'rhistory.html',{'d':a})

def current(request):
	uname=request.user.username
	s=Current.objects.filter(r_uname=uname)
	d=list(s.values())
	a=[]
	for x in d:
		d1=Driver.objects.filter(username=x['d_uname'])
		d1=list(d1.values())
		d1=d1[0]
		d1.update({'pickup':x['pickup']})
		d1.update({'drop':x['drop']})
		a.append(d1)
	return render(request,'rcurrent.html',{'d':a})

def remove(request):
	uname=request.user.username
	duname=request.POST.get('duname','')
	s=Current.objects.filter(d_uname=duname,r_uname=uname).delete()
	#request.sessions['duname']=uname
	return HttpResponseRedirect('/rider/current/')