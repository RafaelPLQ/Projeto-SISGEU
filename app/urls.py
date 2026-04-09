from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lancamentos/', views.lancamentos, name='lancamentos'),
    path('orcamento/', views.orcamento, name='orcamento'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('metas/', views.metas, name='metas'),
    path('alertas/', views.alertas, name='alertas'),
]
