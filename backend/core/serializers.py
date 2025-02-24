# transforma todos os campos do modelo em campos serializáveis ou convertidos para JSON (API)

from rest_framework import serializers
from .models import Partner, Company

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
