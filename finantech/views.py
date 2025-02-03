from django.shortcuts import render
from django.views import View
from .models import *

from .forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView

class IndexView(View):
    def get(self, request):
        context ={
            'contas': Conta.objects.filter(usuario=request.user),
            'total_receitas': Receita.objects.filter(conta__usuario=request.user).aggregate(models.Sum('valor'))['valor__sum'] or 0,
            'total_despesas': Despesa.objects.filter(conta__usuario=request.user).aggregate(models.Sum('valor'))['valor__sum'] or 0,
            'saldo': Conta.objects.filter(usuario=request.user).aggregate(models.Sum('saldo'))['saldo__sum'] or 0
        }
        return render(request, 'index.html', context)


class AdicionarReceitaView(LoginRequiredMixin, CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'adicionar_receita.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('home')


class AdicionarDespesaView(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'adicionar_despesa.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('home')


class AdicionarReceitaView(LoginRequiredMixin, CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'adicionar_receita.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('home')


class AdicionarDespesaView(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'adicionar_despesa.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('home')