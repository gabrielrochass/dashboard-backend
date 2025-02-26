from django.db.models import Count, Avg, Sum, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Partner, Company, Participation
from .serializers import PartnerSerializer, CompanySerializer, ParticipationSerializer, DashboardGeneralStatsSerializer, PartnerStatsSerializer
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
    
class PartnerStatsViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):  # captura o id da url
        try:
            partner = Partner.objects.get(pk=pk)  
        except Partner.DoesNotExist:
            return Response({'error': 'Partner not found'}, status=404)

        # quantidade de empresas que ele é parceiro
        totalCompanies = Participation.objects.filter(partner=partner).values('company').distinct().count()

        # percentual médio de participação dele nas empresas
        avgParticipation = Participation.objects.filter(partner=partner).aggregate(Avg('percentage'))['percentage__avg']

        # maior parceiro
        mostParticipation = Participation.objects.filter(partner=partner).order_by('-percentage').first()

        # menor parceiro
        leastParticipation = Participation.objects.filter(partner=partner).order_by('percentage').first()


        data = {
            'partner': partner.name,
            'totalCompanies': totalCompanies,
            'avgParticipation': avgParticipation,
            'mostParticipation': mostParticipation.company.name if mostParticipation else None,
            'leastParticipation': leastParticipation.company.name if leastParticipation else None,
        }

        return Response(data)

class CompanyStatsViewSet(viewsets.ViewSet):
    serializer_class = PartnerStatsSerializer
    
    def retrieve(self, request, pk=None):  # captura o id da url
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=404)

        # quantidade de parceiros da empresa
        totalPartners = Participation.objects.filter(company=company).values('partner').distinct().count()

        # percentual médio de participação dos parceiros
        avgParticipation = Participation.objects.filter(company=company).aggregate(Avg('percentage'))['percentage__avg']
        
        # top 5 parceiros com maior participação
        topPartners = Participation.objects.filter(company=company).order_by('-percentage')[:5]
        
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
    