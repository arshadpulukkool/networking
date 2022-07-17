from django.shortcuts import render
import os
import socket

# Create your views here.

def home(request):
    return render(request, 'home.html')

def routing(request):
    return render(request, 'routing.html')

def pyth(request):
    return render(request, 'python.html')

def pythonex(request):
    return render(request, 'pythonexamples.html')

