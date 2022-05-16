from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppABM.forms import ClienteForm
from AppClientes.models import Clientes
from django.contrib import messages

# Create your views here.

@login_required
def abm(request): 
    cliente = Clientes.objects.all()
    return render(request, "AppABM/abm.html", {"cli":cliente})

    
@login_required
def agregar_cliente(request):

    data = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El cliente se añadio correctamente")
        else:
            data["form"] = formulario
            
    return render(request, 'AppABM/agregarcliente.html', data)