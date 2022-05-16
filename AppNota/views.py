from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def nota(request): 
    return render(request, "AppNota/nota.html")