from django.shortcuts import render
from django.http import HttpResponse

from app.models import *

# Create your views here.

def home(request):
    return render(request, 'app/homepage.html')

def login(request):
    return render(request, 'app/login.html')

def about(request):
    return render(request, 'app/about.html')

def signup(request):
    return render(request, 'app/signup.html')

    
    ## return HttpResponse("Home sweet homepage")


def specific(request):
    return render(request, 'app/specific.html')


def first(request, variable):
    return HttpResponse("Something" % variable)	



