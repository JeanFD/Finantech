# financas/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .models import Receita, Despesa, Relatorio

@receiver(post_save, sender=Receita)
def atualizar_saldo_despesa(sender, instance, created, **kwargs):

    if created:
        instance.conta.saldo = F('saldo') + instance.valor
        instance.conta.save(update_fields=['saldo'])
    else:
        try:
            old_despesa = Despesa.objects.get(pk=instance.pk)
        except Despesa.DoesNotExist:
            return

        diferenca = old_despesa.valor - instance.valor
        instance.conta.saldo = F('saldo') + diferenca
        instance.conta.save(update_fields=['saldo'])

@receiver(post_delete, sender=Receita)
def reverter_saldo_despesa(sender, instance, **kwargs):
    instance.conta.saldo = F('saldo') - instance.valor
    instance.conta.save(update_fields=['saldo'])


@receiver(post_save, sender=Despesa)
def atualizar_saldo_despesa(sender, instance, created, **kwargs):
    if created:
        instance.conta.saldo = F('saldo') - instance.valor
        instance.conta.save(update_fields=['saldo'])
    else:
        try:
            old_despesa = Despesa.objects.get(pk=instance.pk)
        except Despesa.DoesNotExist:
            return

        diferenca = old_despesa.valor - instance.valor
        instance.conta.saldo = F('saldo') + diferenca
        instance.conta.save(update_fields=['saldo'])

@receiver(post_delete, sender=Despesa)
def reverter_saldo_despesa(sender, instance, **kwargs):
    instance.conta.saldo = F('saldo') + instance.valor
    instance.conta.save(update_fields=['saldo'])

