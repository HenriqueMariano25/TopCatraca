from rest_framework.viewsets import ModelViewSet
from base.models import Bilhetes
from .serializer import BilhetesSerializer

class BilhetesViewSet(ModelViewSet):
    queryset = Bilhetes.objects.all()
    serializer_class = BilhetesSerializer
