from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from django.shortcuts import render

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')
    def post(self, request):
        pass


def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def lancamentos(request):
    return render(request, 'pages/lancamentos.html')

def orcamento(request):
    return render(request, 'pages/orcamento.html')

def relatorios(request):
    return render(request, 'pages/relatorios.html')

def metas(request):
    return render(request, 'pages/metas.html')

def alertas(request):
    return render(request, 'pages/alertas.html')

