<<<<<<< HEAD
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # Login e Cadastro
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),

    # Recuperação de senha
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
=======
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    # Rotas de recuperação de senha (Django built-in)
    path('accounts/password-reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('accounts/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    # Páginas protegidas (requerem login — definido via @login_required em app/views.py)
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lancamentos/', views.lancamentos, name='lancamentos'),
    path('orcamento/', views.orcamento, name='orcamento'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('metas/', views.metas, name='metas'),
    path('alertas/', views.alertas, name='alertas'),
>>>>>>> 481d0b09a52df8e1a6c8079820240659d7f02995
]
