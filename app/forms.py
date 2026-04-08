# accounts/forms.py
from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'curso', 'instituicao', 'data_nascimento']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)