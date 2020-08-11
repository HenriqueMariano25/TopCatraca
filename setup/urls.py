from django.contrib import admin
from django.urls import path, include
from contagem.views import contagemRef
from relatorio.views import relatorioGeral
from rest_framework import routers
# from relatorio.viewsets import BilhetesViewSet
#
# router = routers.DefaultRouter()
# router.register(r'relatorio/todos', BilhetesViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('contagem/ref', contagemRef),
    path('relatorio/geral', relatorioGeral),
    path('admin/', admin.site.urls),
]
