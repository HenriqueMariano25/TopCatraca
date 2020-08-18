from django.shortcuts import render
from relatorio import views

def telasInicial(request):
    return render(request, 'base.html')