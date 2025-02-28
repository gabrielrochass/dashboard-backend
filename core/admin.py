# configura a interface de administração do Django para os modelos de dados do app core
from django.contrib import admin
from .models import Partner, Company, Participation

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
    
@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner', 'company', 'percentage')
    search_fields = ('partner__name', 'company__name')
    ordering = ('id',)
