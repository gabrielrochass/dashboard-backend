from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from decimal import Decimal

class Partner(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    participation = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100.00)])
    company = models.CharField(max_length=100)

    class Meta:
        db_table = 'partners'
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def clean(self):
        from django.db.models import Sum  # evitar conflitos

        errors = []  

        # Validação: soma total das participações por empresa não pode passar de 100
        total_participation = Partner.objects.filter(company=self.company).exclude(pk=self.pk).aggregate(
            total=Sum('participation')
        )['total'] or Decimal(0)

        if total_participation + self.participation > Decimal(100):
            errors.append(f"A soma das participações para a empresa {self.company} não pode ultrapassar 100.00 (atual: {total_participation}).")

        # Validação: participação mínima
        if self.participation < Decimal(0.01):
            errors.append("A participação mínima permitida é 0.01")

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
        
