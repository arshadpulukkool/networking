from django.shortcuts import render
import os
import socket

# Create your views here.

def home(request):
    return render(request, 'home.html')

def osystem(request):
    a = socket.gethostname()
    b = socket.gethostbyname(a)
    print(a)
    return render(request, 'result.html', {'a':a})