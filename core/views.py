# lógica de negócio da aplicação -> camada que faz a comunicação entre o banco de dados e a API

from django.db.models import Count, Avg, Sum, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Partner, Company, Participation
from .serializers import PartnerSerializer, CompanySerializer, ParticipationSerializer, DashboardGeneralStatsSerializer, PartnerStatsSerializer, CompanyStatsSerializer
from .filters import PartnerFilter, CompanyFilter, ParticipationFilter

# viewsets.ModelViewSet -> CRUD
# DjangoFilterBackend -> ativa o filtro
# viewsets.ViewSet -> não é um CRUD, mas um conjunto de operações (list, retrieve, create, update, destroy)
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all() # define quais objetos podem ser acessados
    serializer_class = PartnerSerializer # define qual serializer será utilizado
    
    # filtro -> GET /partners/?name=José
    filter_backends = [DjangoFilterBackend]
    filterset_class = PartnerFilter # define qual filtro será utilizado
    filterset_fields = ['name', 'cpf', 'email'] # define quais campos serão filtrados
    
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
        
        avgPartnersPerCompany = {
            Participation.objects
            .values('company') # agrupa por empresa
            .annotate(total=Count('partner')) # conta quantos parceiros tem em cada empresa
            .aggregate(Avg('total'))['total__avg'] # tira a média de parceiros por empresa
        } 
        
        avgParticipationPerPartner = {
            Participation.objects
            .values('partner')
            .annotate(total=Sum('percentage')) 
            .aggregate(Avg('total'))['total__avg']
        }
        
        companyMostPartners = {
            Company.objects
            .annotate(total=Count('participation')) 
            .order_by('-total') 
            .first()
        }
        
        partnerMostCompanies = {
            Partner.objects
            .annotate(total=Count('participation'))
            .order_by('-total')
            .first()
        }
        
        data = {
            'totalPartners': totalPartners,
            'totalCompanies': totalCompanies,
            'avgPartnersPerCompany': avgPartnersPerCompany,
            'avgParticipationPerPartner': avgParticipationPerPartner,
            'companyMostPartners': companyMostPartners.name,
            'partnerMostCompanies': partnerMostCompanies.name
        }
        
        return Response(data)
    
class PartnerStatsViewSet(viewsets.ViewSet):
    serializer_class = PartnerStatsSerializer
    
    def retrieve(self, request, pk=None):  # captura o id da url
        try:
            partner = Partner.objects.get(pk=pk)  
        except Partner.DoesNotExist:
            return Response({'error': 'Partner not found'}, status=404)

        totalCompanies = {
            Participation.objects.
            filter(partner=partner). 
            values('company').
            distinct().
            count()
        }

        avgParticipation = {
            Participation.objects.
            filter(partner=partner).
            aggregate(Avg('percentage'))['percentage__avg']
        }

        mostParticipation = {
            Participation.objects.
            filter(partner=partner).
            order_by('-percentage').
            first()
        }

        leastParticipation = {
            Participation.objects.
            filter(partner=partner).
            order_by('percentage').
            first()
        }


        data = {
            'partner': partner.name,
            'totalCompanies': totalCompanies,
            'avgParticipation': avgParticipation,
            'mostParticipation': mostParticipation.company.name if mostParticipation else None,
            'leastParticipation': leastParticipation.company.name if leastParticipation else None,
        }

        return Response(data)

class CompanyStatsViewSet(viewsets.ViewSet):
    serializer_class = CompanyStatsSerializer
    
    def retrieve(self, request, pk=None):  # captura o id da url
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=404)

        totalPartners = {
            Participation.objects
            .filter(company=company)
            .values('partner')
            .distinct()
            .count()
        }

        avgParticipation = {
            Participation.objects
            .filter(company=company)
            .aggregate(Avg('percentage'))['percentage__avg']
        }
        
        topPartners = {
            Participation.objects
            .filter(company=company)
            .order_by('-percentage')[:5]
        }
        
        data = {
            'company': company.name,
            'totalPartners': totalPartners,
            'avgParticipation': avgParticipation,
            'topPartners': [
                {
                    'partner': p.partner.name,
                    'percentage': p.percentage
                } for p in topPartners
            ]
        }
        
        return Response(data)
    