from django import forms
from AppClientes.models import Clientes
from AppProveedores.models import Proveedores
from AppArticulos.models import Articulo, Categoria

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

class ClienteModificarForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

class ProveedorModificarForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class ArticuloModificarForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriaModificarForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'