from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import Driver,Rider
from cabsearch.models import History,Current
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login,logout

@login_required(login_url = '/login/driverlogin/')
def dhome(request):
	return render(request,'dhome.html')

@login_required(login_url = '/login/driverlogin/')
def dprofile(request):
	uname=request.user.username
	l=Driver.objects.filter(username=uname)
	l=list(l.values())
	d=l[0]
	return render(request,'dprofile.html',{'d':d})

def dshowhistory(request):
	uname=request.user.username
	s=History.objects.filter(d_uname=uname)
	d=list(s.values())
	a=[]
	for x in d:
		d1=Rider.objects.filter(username=x['r_uname'])
		d1=list(d1.values())
		d1=d1[0]
		d1.update({'pickup':x['pickup']})
		d1.update({'drop':x['drop']})
		a.append(d1)
	return render(request,'rhistory.html',{'d':a})
