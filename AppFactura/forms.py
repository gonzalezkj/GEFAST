from django import forms

from AppFactura.models import DetalleV

class ContactForm(forms.ModelForm):
    class Meta:
        model = DetalleV
        fields = '__all__'