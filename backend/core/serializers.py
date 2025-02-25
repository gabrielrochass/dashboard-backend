# transforma todos os campos do modelo em campos serializáveis ou convertidos para JSON (API)

from rest_framework import serializers
from .models import Partner, Company, Participation

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
    # pra não mostrar diretamente o id, mas sim o nome do parceiro e da empresa
    partnerName = serializers.CharField(source='partner.name', read_only=True)
    companyName = serializers.CharField(source='company.name', read_only=True)
    
    partner = serializers.PrimaryKeyRelatedField(queryset=Partner.objects.all())
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    class Meta:
        model = Participation
        fields = ['id', 'partner', 'company', 'partnerName', 'companyName', 'percentage']