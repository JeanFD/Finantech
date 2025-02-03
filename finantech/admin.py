from django.contrib import admin
from .models import *

admin.site.register(Banco)
admin.site.register(Conta)
admin.site.register(TipoDespesa)
admin.site.register(Despesa)
admin.site.register(TipoReceita)
admin.site.register(Receita)