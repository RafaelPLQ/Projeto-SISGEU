from django.contrib import admin
<<<<<<< HEAD
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
=======
from django.contrib.auth.models import User
from django.contrib.auth import forms

# Register your models here.
class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email','first_name','last_name',)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
>>>>>>> 481d0b09a52df8e1a6c8079820240659d7f02995
