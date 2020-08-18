from django.http import JsonResponse
from base.models import Bilhetes
from datetime import datetime
import datetime


def contagemRef(request):
    if request.method == 'GET':

        hora_inicial = request.GET['hora_inicial']
        print(hora_inicial)

        hora_final = request.GET['hora_final']
        print(hora_final)

        data_original = request.GET['data']
        print(data_original)
        # data_original_formatada = datetime.datetime.strptime(data_original, '%Y-%m-%d').date()

        data_hora_inicial = f"{data_original} {hora_inicial}:00+00:00"
        data_hora_final = f"{data_original} {hora_final}:59+00:00"

        horas = f"{hora_inicial} até {hora_final}"

        refeitorio1 = Bilhetes.objects.select_related().filter(
            datahora__gte=data_hora_inicial, datahora__lte=data_hora_final,numinner__numero__range=(5,8)).order_by('datahora').only('numinner', 'datahora')

        refeitorio2 = Bilhetes.objects.select_related().filter(
            datahora__gte=data_hora_inicial, datahora__lte=data_hora_final,numinner__numero=(9)).order_by('datahora').only('numinner', 'datahora')


        # refeitorio1 = Bilhetes.objects.filter(datahora__day=data_formatada.day, datahora__month=data_formatada.month,
        #                                    datahora__year=data_formatada.year,
        #                                    datahora__time__range=(hora_inicial_formatada, hora_final_formatada),
        #                                    numinner__numero__range=(5,8)
        #                                    ).only('numinner', 'datahora')

        # refeitorio2 = Bilhetes.objects.filter(datahora__day=data_formatada.day, datahora__month=data_formatada.month,
        #                                       datahora__year=data_formatada.year,
        #                                       datahora__time__range=(hora_inicial_formatada, hora_final_formatada),
        #                                       numinner__numero=(9)
        #                                       ).only('numinner', 'datahora')

        resposta = {'refeitorio_1': len(refeitorio1),
                    'refeitorio_2': len(refeitorio2),
                    'data': refeitorio1.first().datahora.strftime("%d/%m/%Y"),
                    'horas': horas}
        return JsonResponse(resposta)
