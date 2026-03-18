from django.db import models

from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    curso = models.CharField(max_length=150, blank=True, null=True)
    instituicao = models.CharField(max_length=200, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome