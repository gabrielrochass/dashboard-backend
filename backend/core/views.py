from rest_framework import viewsets
from .models import Partner, Company
from .serializers import PartnerSerializer, CompanySerializer
from .filters import PartnerFilter
from django_filters.rest_framework import DjangoFilterBackend
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    
    # filtro
    filter_backends = [DjangoFilterBackend]
    filterset_class = PartnerFilter
    search_fields = ['name', 'cpf', 'email']
    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    