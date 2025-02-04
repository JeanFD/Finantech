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

