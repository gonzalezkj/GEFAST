from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def register(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password1')
            usuario = authenticate(username=usuario, password=password)
            login(request, usuario)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to="login")
        data["form"] = formulario
    
    return render(request, 'registration/register.html', data)