from django.db import models
class Partner(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
        
