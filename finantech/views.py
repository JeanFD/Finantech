from django.shortcuts import render
from django.views import View
from .models import *

from .forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, CreateView

class IndexView(View):
    def get(self, request):
        context ={
            'contas': Conta.objects.filter(usuario=request.user),
            'total_receitas': Receita.objects.filter(conta__usuario=request.user).aggregate(models.Sum('valor'))['valor__sum'] or 0,
            'total_despesas': Despesa.objects.filter(conta__usuario=request.user).aggregate(models.Sum('valor'))['valor__sum'] or 0,
            'saldo': Conta.objects.filter(usuario=request.user).aggregate(models.Sum('saldo'))['saldo__sum'] or 0
        }
        return render(request, 'index.html', context)

class ContasView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'contas': Conta.objects.filter(usuario=request.user)
        }
        return render(request, 'contas.html', context)

class ReceitasView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'receitas': Receita.objects.filter(conta__usuario=request.user)
        }
        return render(request, 'receitas.html', context)
    
class TiposReceitasView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'tipos_receitas': TipoReceita.objects.all()
        }
        return render(request, 'tipos_receitas.html', context)

class AdicionarReceitasView(CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'formulario_receita.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        receita = form.save(commit=False)
        receita.conta = form.cleaned_data['conta']
        receita.save()

        return super().form_valid(form)
    
    def get_success_url(self):
         return reverse('home')
    
class AdicionarTiposReceitasView(CreateView):
    model = TipoReceita
    form_class = TipoReceitaForm
    template_name = 'formulario_tipo_receita.html'
    success_url = '/'
    
    def form_valid(self, form):
        banco = form.save(commit=False)
        banco.usuario = self.request.user
        banco.save()

        return super().form_valid(form)
    
    def get_success_url(self):
         return reverse('home')
    
class DespesasView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'despesas': Despesa.objects.filter(conta__usuario=request.user)
        }
        return render(request, 'despesas.html', context)
    
class AdicionarDespesasView(CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'formulario_despesa.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        despesa = form.save(commit=False)
        despesa.conta = form.cleaned_data['conta']
        despesa.save()

        return super().form_valid(form)
    
    def get_success_url(self):
         return reverse('home')
    
class TiposDespesasView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'tipos_despesas': TipoDespesa.objects.all()
        }
        return render(request, 'tipos_despesas.html', context)
    
class AdicionarTiposDespesasView(CreateView):
    model = TipoDespesa
    form_class = TipoDespesaForm
    template_name = 'formulario_tipo_despesa.html'
    success_url = '/'
    
    def form_valid(self, form):
        banco = form.save(commit=False)
        banco.usuario = self.request.user
        banco.save()

        return super().form_valid(form)
    
    def get_success_url(self):
         return reverse('home')

class AdicionarContasView(CreateView):
    model = Conta
    form_class = ContaForm
    template_name = 'formulario_conta.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        conta = form.save(commit=False)
        conta.usuario = self.request.user
        conta.save()

        return super().form_valid(form)
    
    def get_success_url(self):
         return reverse('home')

class BancosView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'bancos': Banco.objects.all()
        }
        return render(request, 'bancos.html', context)
    
class AdicionarBancosView(CreateView):
    model = Banco
    form_class = BancoForm
    template_name = 'formulario_banco.html'
    success_url = '/'
    
    def form_valid(self, form):
        banco = form.save(commit=False)
        banco.usuario = self.request.user
        banco.save()

        return super().form_valid(form)
    
    def get_success_url(self):
         return reverse('home')