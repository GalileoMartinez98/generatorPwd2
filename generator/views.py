from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')
