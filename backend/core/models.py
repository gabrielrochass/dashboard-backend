from django.db import models
from django.core.validators import MinLengthValidator
class Partner(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, validators=[MinLengthValidator(11)])
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Participation(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'{self.partner} ({self.company}) - {self.percentage}%'
    
    class Meta:
        unique_together = ['partner', 'company']

    
        
