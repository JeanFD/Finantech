# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Receita)
def atualizar_saldo_receita(sender, instance, created, **kwargs):
    if created:
        Conta.objects.filter(pk=instance.conta.pk).update(saldo=F('saldo') + instance.valor)
    else:
        valor_antigo = sender.objects.get(pk=instance.pk).valor
        diferenca = instance.valor - valor_antigo
        Conta.objects.filter(pk=instance.conta.pk).update(saldo=F('saldo') + diferenca)

@receiver(post_delete, sender=Receita)
def reverter_saldo_receita(sender, instance, **kwargs):
    Conta.objects.filter(pk=instance.conta.pk).update(saldo=F('saldo') - instance.valor)

# Repita o mesmo para Despesa e Investimento (subtraindo o valor)
@receiver(post_save, sender=Despesa)
def atualizar_saldo_despesa(sender, instance, created, **kwargs):
    if created:
        Conta.objects.filter(pk=instance.conta.pk).update(saldo=F('saldo') - instance.valor)
    else:
        valor_antigo = sender.objects.get(pk=instance.pk).valor
        diferenca = valor_antigo - instance.valor  # Inverte a lógica
        Conta.objects.filter(pk=instance.conta.pk).update(saldo=F('saldo') + diferenca)

@receiver(post_delete, sender=Despesa)
def reverter_saldo_despesa(sender, instance, **kwargs):
    Conta.objects.filter(pk=instance.conta.pk).update(saldo=F('saldo') + instance.valor)