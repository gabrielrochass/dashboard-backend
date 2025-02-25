from rest_framework import viewsets
from .models import Partner, Company, Participation
from .serializers import PartnerSerializer, CompanySerializer, ParticipationSerializer
from .filters import PartnerFilter, CompanyFilter, ParticipationFilter
from django_filters.rest_framework import DjangoFilterBackend
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    
    # filtro
    filter_backends = [DjangoFilterBackend]
    filterset_class = PartnerFilter
    filterset_fields = ['name', 'cpf', 'email']
    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    # filtro
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompanyFilter
    filterset_fields = ['name', 'cnpj', 'address']
    
    
class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    
    # filtro
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParticipationFilter
    filterset_fields = ['partner', 'company', 'percentage']
    
    