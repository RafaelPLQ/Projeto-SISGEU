from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'nome', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'curso', 'instituicao', 'data_nascimento')}),
        ('Permissões', {'fields': ('is_active', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'nome', 'curso', 'instituicao', 'data_nascimento'),
        }),
    )
    search_fields = ('email', 'nome')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Usuario, UsuarioAdmin)