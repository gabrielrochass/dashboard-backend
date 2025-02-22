# Create your models here. -> tabelas do banco de dados (modelos de dados)

from django.db import models
from django.core.validators import MaxValueValidator
class Partner(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    participation = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100.00)])
    class Meta:
        db_table = 'partners'
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
