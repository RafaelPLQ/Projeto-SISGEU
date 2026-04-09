from django.contrib import admin
<<<<<<< HEAD
from .models import Categoria, Orcamento, Despesa, Receita, Meta


=======
from .models import *
from django.contrib import admin

admin.site.register(Usuario)
>>>>>>> 481d0b09a52df8e1a6c8079820240659d7f02995
admin.site.register(Categoria)
admin.site.register(Orcamento)              
admin.site.register(Despesa)
admin.site.register(Receita)
admin.site.register(Meta)
admin.site.register(Alerta)