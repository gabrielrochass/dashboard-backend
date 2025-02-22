# transforma todos os campos do modelo em campos serializáveis ou convertidos para JSON (API)

from rest_framework import serializers
from .models import Partner

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
