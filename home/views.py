from django.shortcuts import render
from django.http import HttpResponse

#create your views here.
def home(request):
    return HttpResponse("Hello, World! This is the home page.")