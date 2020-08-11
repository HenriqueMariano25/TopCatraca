from django.http import JsonResponse
from base.models import Bilhetes
from datetime import datetime


def contagemRef(request):
    if request.method == 'GET':

        hora_inicial = request.GET['hora_inicial']
        hora_inicial_formatada = datetime.strptime(hora_inicial, '%H:%M').time()

        hora_final = request.GET['hora_final']
        hora_final_formatada = datetime.strptime(hora_final, '%H:%M').time()

        data_original = request.GET['data']
        data_formatada = datetime.strptime(data_original, '%d/%m/%Y').date()

        refeitorio1 = Bilhetes.objects.filter(datahora__day=data_formatada.day, datahora__month=data_formatada.month,
                                           datahora__year=data_formatada.year,
                                           datahora__time__range=(hora_inicial_formatada, hora_final_formatada),
                                           numinner__numero__range=(5,8)
                                           ).only('numinner', 'datahora')

        refeitorio2 = Bilhetes.objects.filter(datahora__day=data_formatada.day, datahora__month=data_formatada.month,
                                              datahora__year=data_formatada.year,
                                              datahora__time__range=(hora_inicial_formatada, hora_final_formatada),
                                              numinner__numero=(9)
                                              ).only('numinner', 'datahora')

        resposta = {'refeitorio_1': len(refeitorio1),
                    'refeitorio_2': len(refeitorio2)}
        return JsonResponse(resposta)
