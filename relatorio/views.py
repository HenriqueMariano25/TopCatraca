from django.http import JsonResponse, HttpResponse
from base.models import Bilhetes, Locaisdeacesso
import xlwt
from datetime import datetime
import datetime


def relatorioGeral(request):
    if request.method == 'POST':
        data_inicial = request.POST['data_inicial']
        data_final = request.POST['data_final']
        hora_inicial = request.POST['hora_inicial']
        hora_final = request.POST['hora_final']

        data_inicial_formatada = datetime.datetime.strptime(data_inicial, '%Y-%m-%d').date()
        data_final_formatada = datetime.datetime.strptime(data_final, '%Y-%m-%d').date()

        data_hora_inicial = f"{data_inicial_formatada} {hora_inicial}:00+00:00"
        data_hora_final = f"{data_final_formatada} {hora_final}:59+00:00"

        print(data_hora_inicial)
        print(data_hora_final)


        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="presenca_geral.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Relatorio Geral")

        bilhetes = Bilhetes.objects.select_related().filter(
            datahora__gte=data_hora_inicial, datahora__lte=data_hora_final).order_by('datahora')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Nome', 'Matricula', 'Função', 'Empresa', 'N° Inner', 'Local', 'Hora', 'Data']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()
        rows = bilhetes.values_list('cod_pessoa__funcionarios__nome', 'cod_pessoa__funcionarios__matricula',
                                    'cod_pessoa__funcionarios__cod_departamento__descricao',
                                    'cod_pessoa__funcionarios__cod_departamento__cod_empresa__descricao',
                                    'numinner__numero','cod_local__descricao','datahora','datahora')

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 6:
                    ws.write(row_num, col_num, row[col_num].strftime("%H:%M"), font_style)
                else:
                    if col_num == 7:
                        ws.write(row_num, col_num, row[col_num].strftime("%d/%m/%Y"), font_style)
                    else:
                        ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response

