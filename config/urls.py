from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lancamentos/', views.lancamentos, name='lancamentos'),
    path('orcamento/', views.orcamento, name='orcamento'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('metas/', views.metas, name='metas'),
    path('alertas/', views.alertas, name='alertas'),
]
