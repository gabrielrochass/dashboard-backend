from django.db.models import Count, Avg, Sum, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Partner, Company, Participation
from .serializers import PartnerSerializer, CompanySerializer, ParticipationSerializer, DashboardGeneralStatsSerializer
from .filters import PartnerFilter, CompanyFilter, ParticipationFilter
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
    
class DashboardGeneralStatsViewSet(viewsets.ViewSet):
    serializer_class = DashboardGeneralStatsSerializer
    
    def list(self, request):
        totalPartners = Partner.objects.count()
        totalCompanies = Company.objects.count()
        avgParnersPerCompany = Participation.objects.values('company').annotate(total=Count('partner')).aggregate(Avg('total'))['total__avg']
        avgParticipationPerPartner = Participation.objects.values('partner').annotate(total=Sum('percentage')).aggregate(Avg('total'))['total__avg']
        
        # empresa com mais parceiros
        companyMostPartners = Company.objects.annotate(total=Count('participation')).order_by('-total').first()
        
        # parceiro com mais empresas particiopando
        partnerMostCompanies = Partner.objects.annotate(total=Count('participation')).order_by('-total').first()
        
        data = {
            'totalPartners': totalPartners,
            'totalCompanies': totalCompanies,
            'avgParnersPerCompany': avgParnersPerCompany,
            'avgParticipationPerPartner': avgParticipationPerPartner,
            'companyMostPartners': companyMostPartners.name,
            'partnerMostCompanies': partnerMostCompanies.name
        }
        
        return Response(data)
    
    