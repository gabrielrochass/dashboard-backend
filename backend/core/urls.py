# define as rotas do app "core"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet, CompanyViewSet, ParticipationViewSet, DashboardGeneralStatsViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'participations', ParticipationViewSet)
router.register(r'dashboard-general-stats', DashboardGeneralStatsViewSet, basename='dashboard-general-stats')

urlpatterns = [
    path('', include(router.urls)),
]
