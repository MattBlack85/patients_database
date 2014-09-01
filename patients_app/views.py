from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("you are in index")

def edit(request, name):
    return HttpResponse("edit patient %s" % name)

