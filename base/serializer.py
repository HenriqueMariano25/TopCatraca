from rest_framework import serialzers
from base.models import Empresas

class EmpresasSerializer(serialzers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'