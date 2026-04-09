# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CadastroForm, LoginForm
from .models import Usuario
from django.contrib.auth.decorators import login_required


def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])
            usuario.save()
            return redirect('accounts:login')
    else:
        form = CadastroForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('app:dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('app:dashboard')
            else:
                form.add_error(None, 'E-mail ou senha inválidos.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
