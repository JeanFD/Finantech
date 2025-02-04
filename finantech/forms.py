from django import forms
from .models import *

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['nome', 'banco']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            True

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['valor', 'data', 'descricao', 'conta', 'tipo']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['conta'].queryset = Conta.objects.filter(usuario=user)

class TipoReceitaForm(forms.ModelForm):
    class Meta:
        model = TipoReceita
        fields = ['nome']

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['valor', 'data', 'descricao', 'conta', 'tipo']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['conta'].queryset = Conta.objects.filter(usuario=user)

class TipoDespesaForm(forms.ModelForm):
    class Meta:
        model = TipoDespesa
        fields = ['nome']

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nome']