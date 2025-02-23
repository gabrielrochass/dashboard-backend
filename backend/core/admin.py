from django.contrib import admin
import django_filters
from django.utils.translation import gettext_lazy as _
from .models import Partner

# Criar um FilterSet para pesquisa no Django Admin
class PartnerFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(lookup_expr='icontains')
    firstName = django_filters.CharFilter(lookup_expr='icontains')
    lastName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Partner
        fields = ['company', 'firstName', 'lastName']

# Configuração do Admin para Partner
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "company")  # Exibir no Admin
    list_filter = ("company",)  # Adiciona filtros laterais
    search_fields = ("firstName", "lastName", "company")  # Adiciona campo de busca

admin.site.register(Partner, PartnerAdmin)
