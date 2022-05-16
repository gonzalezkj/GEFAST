from django import forms
from AppArticulos.models import Articulo

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
        exclude = ['disponibilidad']

#class ModificarForm(forms.ModelForm):
#    class Meta:
#        model = Product
#        fields = '__all__'