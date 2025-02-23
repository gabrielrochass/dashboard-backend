from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .models import Partner
from .serializers import PartnerSerializer
from .filters import PartnerFilter
from django_filters.rest_framework import DjangoFilterBackend

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = PartnerFilter
    filterset_fields = ['company', 'firstName', 'lastName', 'participation']
    
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            try:
                partner = Partner(**serializer.validated_data)
                partner.full_clean()  # Validação manual antes de salvar
                partner.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"erro": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
