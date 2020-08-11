from django.http import JsonResponse
from base.models import Bilhetes, Locaisdeacesso
from rest_framework import viewsets
from datetime import datetime


def relatorioGeral(request):
    if request.method == 'GET':
        # data_original = request.GET['data']
        # data_formatada = datetime.strptime(data_original, '%d/%m/%Y').date()

        bilhetes = Locaisdeacesso.objects.all()
        # for bilhete in bilhetes:
        #     print("bilhete.datahora")

        # print(len(bilhetes))

        resposta = {
            'ref': len(bilhetes)
        }
        return JsonResponse(resposta)
