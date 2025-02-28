# define os filtros para os modelos
import django_filters
from .models import Partner, Company, Participation

# lookup_expr -> operador de comparação
# icontains -> case insensitive
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

class ParticipationFilter(django_filters.FilterSet):
    partner = django_filters.CharFilter(field_name="partner__name", lookup_expr="icontains", label="Partner Name")
    company = django_filters.CharFilter(field_name="company__name", lookup_expr="icontains", label="Company Name")
    percentage = django_filters.NumberFilter(field_name="percentage", lookup_expr="exact", label="Participation (%)")

    class Meta:
        model = Participation
        fields = ["partner", "company", "percentage"]
