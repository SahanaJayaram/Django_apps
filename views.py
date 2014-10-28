from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import context, RequestContext
from django.core.context_processors import csrf
from stars.models import Person
#from forms import PersonForm
from stars.models import Login_details
#from forms import LoginForm

# Create your views here.

def home(request):
	return render(request,"hello.html")

def Person_list(request):
	entries=Person.objects.all()
	return render(request,"Persons.html",{"Person":entries})

def Login_list(request):
	data=Login_details.objects.all()
	return render(request,"Logins.html",{"Login_details":data})


def registration(request): 
		return render(request,"registration.html")


def login(request):
	return render(request,"login.html")
