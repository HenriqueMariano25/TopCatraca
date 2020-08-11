from rest_framework.serializers import ModelSerializer
from base.models import Bilhetes

class BilhetesSerializer(ModelSerializer):
    class Meta:
        model = Bilhetes
        fields = ['numinner']