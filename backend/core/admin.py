from django.contrib import admin
from .models import Partner, Company

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'email')
    search_fields = ('name', 'cpf')
    ordering = ('id',)
    

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'address')
    search_fields = ('name', 'cnpj')
    ordering = ('id',)
    
