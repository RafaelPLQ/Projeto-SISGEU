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
