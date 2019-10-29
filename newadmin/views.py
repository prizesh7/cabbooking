from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from signup.models import Driver


def login(request):
	print("*************")
	return render(request,'login.html')

def validateadmin(request):
	uname=request.POST.get('uname','')
	passw=request.POST.get('pass','')
	if uname=='user1' and passw=='123':
		return render(request,'loggedin.html')
	else:
		return render(request,'login.html')

def viewdriver(request):
	i=Driver.objects.all()
	i=list(i.values())
	d=i
	return render(request,'display.html',{'d':d})

