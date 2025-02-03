from django import forms
from .models import Receita, Despesa, Conta

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['valor', 'data', 'descricao', 'conta', 'tipo']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['conta'].queryset = Conta.objects.filter(usuario=user)


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['valor', 'data', 'descricao', 'conta', 'tipo']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['conta'].queryset = Conta.objects.filter(usuario=user)

