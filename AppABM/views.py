from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from AppABM.forms import ArticuloForm, ArticuloModificarForm, CategoriaForm, CategoriaModificarForm, ClienteForm, ClienteModificarForm, ProveedorForm, ProveedorModificarForm, UsuarioForm, UsuarioModificarForm
from AppClientes.models import Clientes
from AppProveedores.models import Proveedores
from django.contrib import messages
from AppProveedores.models import Proveedores
from AppArticulos.models import Articulo, Categoria
from django.contrib.auth.models import User

# Create your views here.

@login_required
def abm(request): 
    cliente = Clientes.objects.all()
    return render(request, "AppABM/abm.html", {"cli":cliente})

@login_required
def abmproveedor(request): 
    proveedor = Proveedores.objects.all()
    return render(request, "AppABM/abmproveedor.html", {"pro":proveedor})

@login_required
def abmarticulo(request): 
    articulo = Articulo.objects.all()
    return render(request, "AppABM/abmarticulo.html", {"art":articulo})
    
@login_required
def abmcategoria(request): 
    categoria = Categoria.objects.all()
    return render(request, "AppABM/abmcategoria.html", {"cat":categoria})

@login_required
def abmusuario(request): 
    usuario = User.objects.all()
    return render(request, "AppABM/abmusuario.html", {"user":usuario})

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

@login_required
def modificar_cliente(request, id):

    producto = get_object_or_404(Clientes, id_cliente=id)

    data = {
        'form': ClienteModificarForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ClienteModificarForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "The product has been modify correctly")
        else:
            data["form"] = formulario
        
    return render(request, 'AppABM/modificarcliente.html', data)

@login_required
def agregar_proveedor(request):

    data = {
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El proveedor se añadio correctamente")
        else:
            data["form"] = formulario
            
    return render(request, 'AppABM/agregarproveedor.html', data)

@login_required
def modificar_proveedor(request, id):

    producto = get_object_or_404(Proveedores, id_proveedor=id)

    data = {
        'form': ProveedorModificarForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProveedorModificarForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El proveedor se modifico correctamente")
        else:
            data["form"] = formulario
        
    return render(request, 'AppABM/modificarcliente.html', data)

@login_required
def agregar_articulo(request):

    data = {
        'form': ArticuloForm()
    }

    if request.method == 'POST':
        formulario = ArticuloForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El articulo se añadio correctamente")
        else:
            data["form"] = formulario
            
    return render(request, 'AppABM/agregararticulo.html', data)

@login_required
def modificar_articulo(request, id):

    producto = get_object_or_404(Articulo, id_articulo=id)

    data = {
        'form': ArticuloModificarForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ArticuloModificarForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El articulo se modifico correctamente")
        else:
            data["form"] = formulario
        
    return render(request, 'AppABM/modificararticulo.html', data)

@login_required
def agregar_categoria(request):

    data = {
        'form': CategoriaForm()
    }

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La categoria se añadio correctamente")
        else:
            data["form"] = formulario
            
    return render(request, 'AppABM/agregarcategoria.html', data)

@login_required
def modificar_categoria(request, id):

    producto = get_object_or_404(Categoria, id_categoria=id)

    data = {
        'form': CategoriaModificarForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = CategoriaModificarForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La categoria se modifico correctamente")
        else:
            data["form"] = formulario
        
    return render(request, 'AppABM/modificarcategoria.html', data)

@login_required
def agregar_usuario(request):

    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El usuario se añadio correctamente")
        else:
            data["form"] = formulario
            
    return render(request, 'AppABM/agregarusuario.html', data)

@login_required
def modificar_usuario(request, id):

    producto = get_object_or_404(User, id=id)

    data = {
        'form': UsuarioModificarForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = UsuarioModificarForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El usuario se modifico correctamente")
        else:
            data["form"] = formulario
        
    return render(request, 'AppABM/modificarusuario.html', data)