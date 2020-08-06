from django.http import JsonResponse
from base.models import Empresas

def contagemRef(request):
    if request.method == 'GET':
        empresas = Empresas.objects.all()
        print(empresas)
        ref = {'ref1':10, 'ref2':20}
        return JsonResponse(ref)