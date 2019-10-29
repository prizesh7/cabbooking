from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required


def home(request):
	c = {}
	c.update(csrf(request))
	return render(request,'home.html', c)

def about(request):
	return render(request,'about.html')

def rental(request):
	return render(request,'rental.html')

def citytaxi(request):
	return render(request,'citytaxi.html')

def news(request):
	return render(request,'news.html')

def outstation(request):
	return render(request,'outstation.html')

def contact(request):
	return render(request,'contact.html')