from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def barra(request): 
    if request.user.is_authenticated:
        print(f"Username: {request.user.email}")
    else:
        print("User is not logged in")