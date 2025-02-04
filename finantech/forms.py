from django import forms
from .models import *

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['nome', 'banco']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        if user:
            pass  # Você pode adicionar lógica específica para o usuário aqui


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['valor', 'data', 'descricao', 'conta', 'tipo']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        if user:
            self.fields['conta'].queryset = Conta.objects.filter(usuario=user)


class TipoReceitaForm(forms.ModelForm):
    class Meta:
        model = TipoReceita
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['valor', 'data', 'descricao', 'conta', 'tipo']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        if user:
            self.fields['conta'].queryset = Conta.objects.filter(usuario=user)


class TipoDespesaForm(forms.ModelForm):
    class Meta:
        model = TipoDespesa
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['nome', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
