import django_filters
from .models import Partner

class PartnerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    cpf = django_filters.CharFilter(lookup_expr='icontains', label='CPF')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')
    
    class Meta:
        model = Partner
        fields = ['name', 'cpf', 'email']
