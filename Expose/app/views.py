from django.shortcuts import responsender
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello fellas")


def first(request, variable):
    return HttpResponse("Something" % variable)	


