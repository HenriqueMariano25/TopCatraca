from django.contrib import admin
from django.urls import path
from contagem.views import contagemRef

urlpatterns = [
    path('contagem/ref', contagemRef),
    path('admin/', admin.site.urls),
]
