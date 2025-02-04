from django.db import models
from django.contrib.auth.models import User

class Banco(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return self.nome


class Conta(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Saldo", default=0)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, verbose_name="Banco")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return f'{self.nome} - {self.banco.nome}'


class TipoDespesa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    class Meta:
        verbose_name = "Tipo de Despesa"
        verbose_name_plural = "Tipos de Despesas"

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data")
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name="Conta")
    tipo = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE, verbose_name="Tipo de Despesa")

    class Meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"

    def __str__(self):
        return f'{self.descricao} - {self.data}'


class TipoReceita(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    class Meta:
        verbose_name = "Tipo de Receita"
        verbose_name_plural = "Tipos de Receitas"

    def __str__(self):
        return self.nome


class Receita(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data")
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name="Conta")
    tipo = models.ForeignKey(TipoReceita, on_delete=models.CASCADE, verbose_name="Tipo de Receita")

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __str__(self):
        return f'{self.descricao} - {self.data}'

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Relatorio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")

    despesa_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Despesa Total", default=0)
    receita_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Receita Total", default=0)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Saldo", default=0)

    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"
        ordering = ['-data_inicio']

    def __str__(self):
        return f"Relatório {self.nome} - {self.data_inicio} a {self.data_fim}"

    def calcular_totais(self):
        despesas = Despesa.objects.filter(
            conta__usuario=self.usuario,
            data__range=(self.data_inicio, self.data_fim)
        ).aggregate(total=Sum('valor'))['total'] or 0

        receitas = Receita.objects.filter(
            conta__usuario=self.usuario,
            data__range=(self.data_inicio, self.data_fim)
        ).aggregate(total=Sum('valor'))['total'] or 0

        self.despesa_total = despesas
        self.receita_total = receitas
        self.saldo = receitas - despesas
        print(f'\n\n\n\n\n {despesas}')

    def save(self, *args, **kwargs):
        super(Relatorio, self).save(*args, **kwargs)
        self.calcular_totais()
        super(Relatorio, self).save(update_fields=['despesa_total', 'receita_total', 'saldo'])
