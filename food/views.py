from django.shortcuts import render
from django.http import HttpResponse

def vegetarian(request):
    return HttpResponse('<h1>I like vegetarian foods like kalan briyani,poori redgravy,veg-briyani,etc...</h1>')

def nonveg(request):
    return render(request,'nonveg.html')

# Create your views here.
