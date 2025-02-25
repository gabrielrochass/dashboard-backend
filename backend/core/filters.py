import django_filters
from .models import Partner, Company

class PartnerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    cpf = django_filters.CharFilter(lookup_expr='icontains', label='CPF')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')
    
    class Meta:
        model = Partner
        fields = ['name', 'cpf', 'email']
        
        
class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    cnpj = django_filters.CharFilter(lookup_expr='icontains', label='CNPJ')
    address = django_filters.CharFilter(lookup_expr='icontains', label='Address')
    
    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'address']
