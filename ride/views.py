from django.shortcuts import render
from django.http import HttpResponse

def bike(request):
    return HttpResponse('<h1>I like to ride royal-enfield </h1>')

# Create your views here.
