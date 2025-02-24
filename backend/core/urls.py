# define as rotas do app "core"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
