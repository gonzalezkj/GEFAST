from django.shortcuts import render

# Create your views here.

def nota(request): 
    return render(request, "AppNota/nota.html")