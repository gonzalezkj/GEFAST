from django import forms
from AppClientes.models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
