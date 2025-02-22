# Create your views here. -> lógica das requisições

from rest_framework import viewsets
from .models import Partner
from .serializers import PartnerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# foco em participação
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer