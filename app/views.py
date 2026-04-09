<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def dashboard(request):
    """
    View do dashboard - página principal após login
    """
    context = {
        'title': 'Dashboard',
        'user': request.user,
    }
    return render(request, 'pages/dashboard.html', context)


@login_required(login_url='accounts:login')
def lancamentos(request):
    """
    View da página de lançamentos
    """
    context = {
        'title': 'Lançamentos',
        'user': request.user,
    }
    return render(request, 'pages/lancamentos.html', context)


@login_required(login_url='accounts:login')
def orcamento(request):
    """
    View da página de orçamento
    """
    context = {
        'title': 'Orçamento',
        'user': request.user,
    }
    return render(request, 'pages/orcamento.html', context)


@login_required(login_url='accounts:login')
def relatorios(request):
    """
    View da página de relatórios
    """
    context = {
        'title': 'Relatórios',
        'user': request.user,
    }
    return render(request, 'pages/relatorios.html', context)


@login_required(login_url='accounts:login')
def metas(request):
    """
    View da página de metas
    """
    context = {
        'title': 'Metas',
        'user': request.user,
    }
    return render(request, 'pages/metas.html', context)


@login_required(login_url='accounts:login')
def alertas(request):
    """
    View da página de alertas
    """
    context = {
        'title': 'Alertas',
        'user': request.user,
    }
    return render(request, 'pages/alertas.html', context)
=======
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
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'E-mail ou senha inválidos.')
    else:
        form = LoginForm()
    # ← CORRIGIDO: template correto (registration/login.html, dentro de accounts/templates/)
    return render(request, 'registration/login.html', {'form': form})
>>>>>>> 481d0b09a52df8e1a6c8079820240659d7f02995
