from django.db import models

# Create your models here.
class Conta(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Saldo")
    banco = models.foreingKey("Banco", on_delete=models.CASCADE, verbose_name="Banco")

    class meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return f'{self.nome} + " - " + {self.banco.nome}'
        

class Banco(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    class meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data")
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    conta = models.foreingKey("Conta", on_delete=models.CASCADE, verbose_name="Conta")
    tipo = models.foreingKey("TipoDespesa", on_delete=models.CASCADE, verbose_name="Tipo de Despesa")
    class meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"

    def __str__(self):
        return f'{self.descricao} + " - " + {self.data}'


class TipoDespesa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    class meta:
        verbose_name = "Tipo de Despesa"
        verbose_name_plural = "Tipos de Despesas"

    def __str__(self):
        return self.nome


class Receita(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data")
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    conta = models.foreingKey("Conta", on_delete=models.CASCADE, verbose_name="Conta")
    tipo = models.foreingKey("TipoReceita", on_delete=models.CASCADE, verbose_name="Tipo de Receita")

    class meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __str__(self):
        return f'{self.descricao} + " - " + {self.data}'


class TipoReceita(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    class meta:
        verbose_name = "Tipo de Receita"
        verbose_name_plural = "Tipos de Receitas"

    def __str__(self):
        return self.nome
    

class Investimento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data")
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    conta = models.foreingKey("Conta", on_delete=models.CASCADE, verbose_name="Conta")
    tipo = models.foreingKey("TipoInvestimento", on_delete=models.CASCADE, verbose_name="Tipo de Investimento")

    class meta:
        verbose_name = "Investimento"
        verbose_name_plural = "Investimentos"

    def __str__(self):
        return f'{self.descricao} + " - " + {self.data}'
    

class TipoInvestimento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    class meta:
        verbose_name = "Tipo de Investimento"
        verbose_name_plural = "Tipos de Investimentos"

    def __str__(self):
        return self.nome
    

class Relatorio(models.Model):
    data_inicio = models.DateField(verbose_name="Data Início")
    data_fim = models.DateField(verbose_name="Data Fim")

    class meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"

    def __str__(self):
        return f'{self.data_inicio} + " - " + {self.data_fim}'