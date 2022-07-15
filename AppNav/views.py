from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def barra(request): 
    usuario = User.objects.all()
    return render(request, "AppNav/barra.html")