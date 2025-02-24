import django_filters
from .models import Partner

class PartnerFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name="company", lookup_expr='icontains') # checa se o campo contém o valor (case insensitive)
    # min_participation = django_filters.NumberFilter(field_name="participation", lookup_expr='gte')
    # max_participation = django_filters.NumberFilter(field_name="participation", lookup_expr='lte')
    firstName = django_filters.CharFilter(field_name="firstName", lookup_expr='icontains')
    lastName = django_filters.CharFilter(field_name="lastName", lookup_expr='icontains')

    class Meta:
        model = Partner
        fields = ['company', 'firstName', 'lastName']
