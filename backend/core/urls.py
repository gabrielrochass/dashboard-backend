from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Define a rota inicial do app "core"
]
