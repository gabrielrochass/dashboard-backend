# define as rotas do app "core"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet, CompanyViewSet, ParticipationViewSet, DashboardGeneralStatsViewSet, PartnerStatsViewSet, CompanyStatsViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'participations', ParticipationViewSet)
# define basename pq não é um CRUD (viewset.ViewSet)
router.register(r'dashboard-general-stats', DashboardGeneralStatsViewSet, basename='dashboard-general-stats') 
router.register(r'partner-stats', PartnerStatsViewSet, basename='partner-stats')
router.register(r'company-stats', CompanyStatsViewSet, basename='company-stats')

urlpatterns = [
    path('', include(router.urls)),
]
