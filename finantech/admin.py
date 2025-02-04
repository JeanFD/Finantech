from django.contrib import admin
from .models import *


class ContaInline(admin.TabularInline):
    model = Conta
    extra = 1

class ReceitaInline(admin.TabularInline):
    model = Receita
    extra = 1

class DespesaInline(admin.TabularInline):
    model = Despesa
    extra = 1

class UsuarioInline(admin.TabularInline):
    model = User
    extra = 1

class TipoDespesaInline(admin.TabularInline):
    model = TipoDespesa
    extra = 1

class TipoReceitaInline(admin.TabularInline):
    model = TipoReceita
    extra = 1

class RelatorioInline(admin.TabularInline):
    model = Relatorio
    extra = 1

class BancoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [ContaInline]

class ContaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [DespesaInline, ReceitaInline]

class TipoDespesaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [DespesaInline]

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data', 'descricao', 'conta', 'tipo')
    search_fields = ('valor', 'data', 'descricao', 'conta', 'tipo')

class TipoReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [ReceitaInline]

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data', 'descricao', 'conta', 'tipo')
    search_fields = ('valor', 'data', 'descricao', 'conta', 'tipo')

class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('nome','data_inicio','data_fim')
    search_fields = ('nome',)

admin.site.register(Banco, BancoAdmin)
admin.site.register(Conta, ContaAdmin)
admin.site.register(TipoDespesa, TipoDespesaAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(TipoReceita, TipoReceitaAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Relatorio, RelatorioAdmin)