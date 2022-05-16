from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(min_length=4, max_length=30, widget= forms.TextInput(attrs= {'placeholder':"Usuario"}))

    first_name = forms.CharField (min_length =2, max_length = 50, widget= forms.TextInput(attrs= {'placeholder':'Nombre'}))

    last_name= forms.CharField (min_length =2, max_length = 50, widget= forms.TextInput(attrs= {'placeholder':'Apellido'}))

    email = forms.EmailField(min_length=6, max_length= 70, widget=forms.EmailInput(attrs= {'placeholder':'Email'}))

    password1 = forms.CharField (max_length = 70, widget=forms.PasswordInput(attrs= {'placeholder':'Contraseña'}))

    password2 = forms.CharField (max_length =70, widget=forms.PasswordInput(attrs= {'placeholder':'Confirmar contraseña '}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        exist = User.objects.filter(email__iexact=email).exists()

        if exist:
            raise forms.ValidationError("Este email ya existe, por favor intentá con otro.")
        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
