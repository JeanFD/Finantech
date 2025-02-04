from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('contas/', ContasView.as_view(), name='contas'),
    path('adicionar_conta/', AdicionarContasView.as_view(), name='adicionar_conta'),
    path('receitas/', ReceitasView.as_view(), name='receitas'),
    path('adicionar_receita/', AdicionarReceitasView.as_view(), name='adicionar_receita'),
    path('tipos_receitas/', TiposReceitasView.as_view(), name='tipos_receitas'),
    path('adicionar_tipos_receitas/', AdicionarTiposReceitasView.as_view(), name='adicionar_tipos_receitas'),
    path('despesas/', DespesasView.as_view(), name='despesas'),
    path('adicionar_despesa/', AdicionarDespesasView.as_view(), name='adicionar_despesa'),
    path('tipos_despesas/', TiposDespesasView.as_view(), name='tipos_despesas'),
    path('adicionar_tipo_despesa/', AdicionarTiposDespesasView.as_view(), name='adicionar_tipo_despesa'),
    path('bancos/', BancosView.as_view(), name='bancos'),
    path('adicionar_bancos/', AdicionarBancosView.as_view(), name='adicionar_banco'),
]
