from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import Rider,Driver,Availabledriver
from cabsearch.models import Cabdriver,History,Current
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.contrib import messages

@login_required(login_url = '/login/riderlogin/')
def searchcab(request):
	pickup = request.POST.get('pickup', '')
	drop = request.POST.get('drop', '')
	texitype = request.POST.get('texitype', '')
	if pickup==drop:
		messages.add_message(request,messages.WARNING,'Same source and Destination')
		return render(request,'rhome.html')
	else:
		d={}
		d.update({'pickup':pickup})
		d.update({'drop':drop})
		d.update({'texitype':texitype})
		return render(request,'confirm.html',{'d':d})


@login_required(login_url = '/login/riderlogin/')
def confirm(request):
	pickup = request.POST.get('pickup', '')
	drop = request.POST.get('drop', '')
	texitype=request.POST.get('texitype', '')
	l=Availabledriver.objects.filter()
	d=list(l.values())
	d=d[0]
	s=Current(r_uname=request.user.username,d_uname=d['username'],pickup=pickup,drop=drop)
	s.save()
	print(pickup,drop,texitype)
	otp = get_random_string(6, allowed_chars='0123456789')
	print(otp)
	s=Current(r_uname=request.user.username,d_uname=d['username'],pickup=pickup,drop=drop,otp=otp)
	s.save()
	s=Cabdriver(username=d['username'],otp=otp,pickup=pickup,drop=drop)
	s.save()
	if len(d)==0:
		return render(request,'tryagain.html')
	else:
		request.session['uname']=d['username']
		request.session['otp']=otp
		return HttpResponseRedirect('/mail/sendemail/')

@login_required(login_url = '/login/driverlogin/')
def verify(request):
	uname=request.user.username
	otp = request.POST.get('otp', '')
	l=Cabdriver.objects.filter(username=uname)
	d=list(l.values())
	d=d[0]
	if d['otp']==otp:
		l=Availabledriver.objects.filter(username=uname).delete()
		return render(request,'valid.html')
	else:
		messages.add_message(request,messages.WARNING,'Incorrect Username or password')
		return render(request,'dhome.html')


@login_required(login_url = '/login/driverlogin/')
def endtrip(request):
	uname = request.user.username
	l=Driver.objects.filter(username=uname)
	d=list(l.values())
	d=d[0]
	l=Cabdriver.objects.filter(username=uname).delete()
	s=Availabledriver(username=d['username'],fname=d['fname'],lname=d['lname'],phone_no=d['phone_no'])
	s.save()
	d=Current.objects.filter(d_uname=uname)
	d=list(d.values())
	d=d[0]
	s=History(username=d['username'],otp=otp,pickup=pickup,drop=drop)
	s.save()
	d=Current.objects.filter(d_uname=uname).delete()
	return HttpResponseRedirect('/driver/dhome/')
