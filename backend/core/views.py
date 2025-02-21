from django.shortcuts import render

# Create your views here. -> lógica das requisições

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, bem-vindo ao backend!")
