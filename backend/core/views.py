# Create your views here. -> lógica das requisições

from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['name']
    search_fields = ['name', 'address', 'phone', 'website']
    ordering_fields = ['name', 'address', 'phone', 'website']
    ordering = ['name']
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['company']
    search_fields = ['firstName', 'lastName', 'email', 'phone']
    ordering_fields = ['firstName', 'lastName', 'email', 'phone']
    ordering = ['firstName']
 
class MetricsView(APIView):
    def get(self, request):
        total_companies = Company.objects.count()
        total_employees = Employee.objects.count()
        avg_employees_per_company = total_employees / total_companies if total_companies > 0 else 0
        max_employees_in_company = Employee.objects.values('company').annotate(count=Count('id')).order_by('-count').first()
        max_employees_in_company = max_employees_in_company['count'] if max_employees_in_company else 0

        min_employees_in_company = Employee.objects.values('company').annotate(count=Count('id')).order_by('count').first()
        min_employees_in_company = min_employees_in_company['count'] if min_employees_in_company else 0

        metrics = {
            "Total Companies": total_companies,
            "Total Employees": total_employees,
            "Average Employees per Company": avg_employees_per_company,
            "Maximum Employees per Company": max_employees_in_company,
            "Minimum Employees per Company": min_employees_in_company
        }
        return Response(metrics)