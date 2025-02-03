from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('adicionar-receita/', AdicionarReceitaView.as_view(), name='adicionar_receita'),
    path('adicionar-despesa/', AdicionarDespesaView.as_view(), name='adicionar_despesa'),
]
