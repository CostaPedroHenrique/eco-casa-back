from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.
class Balance(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    total = models.DecimalField(
        verbose_name='Total',
        max_digits=9, 
        decimal_places=2
    )

    def __str__(self):
        return "Saldo: #{}".format(self.total)

    class Meta:
        app_label="deposit"
        verbose_name="Saldo"
        verbose_name_plural="Saldos"

class Material(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=50,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label="deposit"
        verbose_name="Material"
        verbose_name_plural="Materiais"

class Deposit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.SET_NULL,
        null=True
    )

    weight = models.DecimalField(
        verbose_name='Peso',
        max_digits=5, 
        decimal_places=2
    )

    value = models.DecimalField(
        verbose_name='Valor',
        max_digits=5, 
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "Deposito: #{}".format(self.id)

    class Meta:
        app_label="deposit"
        verbose_name="Deposito"
        verbose_name_plural="Depositos"