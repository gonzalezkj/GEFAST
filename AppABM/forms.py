from django import forms
from AppClientes.models import Clientes
from AppProveedores.models import Proveedores
from AppArticulos.models import Articulo, Categoria
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['razon_nombre', 'cuit', 'condicion', 'telefono']

class ClienteModificarForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['razon_nombre', 'cuit', 'condicion', 'telefono']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['razon_social', 'cuit', 'condicion', 'telefono', 'email', 'direccion']

class ProveedorModificarForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['razon_social', 'cuit', 'condicion', 'telefono', 'email']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'categoria', 'precio', 'cantidad']

class ArticuloModificarForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'categoria', 'precio', 'cantidad']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class CategoriaModificarForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class UsuarioModificarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']