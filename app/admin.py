from django.contrib import admin
from .models import Categoria, Orcamento, Despesa, Receita, Meta


admin.site.register(Categoria)
admin.site.register(Orcamento)              
admin.site.register(Despesa)
admin.site.register(Receita)
admin.site.register(Meta)
admin.site.register(Alerta)