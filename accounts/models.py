# accounts/models.py
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, senha, curso, instituicao, data_nascimento):
        if not email:
            raise ValueError('O email é obrigatório')
        user = self.model(
            id=uuid.uuid4(),
            email=self.normalize_email(email),
            nome=nome,
            curso=curso,
            instituicao=instituicao,
            data_nascimento=data_nascimento
        )
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, senha, curso, instituicao, data_nascimento):
        user = self.create_user(email, nome, senha, curso, instituicao, data_nascimento)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=255)
    curso = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'curso', 'instituicao', 'data_nascimento']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin# accounts/forms.py
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