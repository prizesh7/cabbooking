from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from signup.models import Rider,Driver,Availabledriver
from django.contrib.auth.decorators import login_required
from cabsearch.models import Cabdriver
from signup.models import Availabledriver

import smtplib


# Create your views here.


def sendemail(request):
	l=Availabledriver.objects.filter(username=request.session['uname'])
	d=list(l.values())
	d=d[0]
	otp=request.session['otp']
	d.update({'otp':otp})
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login("prizeshbhadaniya@gmail.com","prizesh345")
	uname = request.user.username
	email= request.user.email
	msg='To:'+ email+'\n'+'From:prizeshbhadaniya@gmail.com'+'\n'+'Subject:otp\n'
	msg=msg + "hello  " +uname+'\n'+ "your verify otp is  " +otp
	server.sendmail("prizeshbhadaniya@gmail.com",email,msg)
	return render(request,'driverinfo.html',{'d':d})

def info_cansle(request):
	runame=request.user.username
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login("prizeshbhadaniya@gmail.com","mail password")
	l=Driver.objects.filter(username=duname)
	l=list(l.values())
	l=l[0]
	email=l['email']
	msg='To:'+ email+'\n'+'From:prizeshbhadaniya@gmail.com'+'\n'+'Subject:otp\n'
	msg=msg + "hello  " +duname+'\n'+ "your request from"+runame +"\n ride is cansle"
	server.sendmail("prizeshbhadaniya@gmail.com",email,msg)
	return HttpResponseRedirect('/rider/current/')
