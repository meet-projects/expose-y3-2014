from django.shortcuts import render
from django.http import HttpResponse

from app.models import *

# Create your views here.

def home(request):
    return render(request, 'app/index.html')
    
    ## return HttpResponse("Home sweet homepage")


def first(request, variable):
    return HttpResponse("Something" % variable)	



