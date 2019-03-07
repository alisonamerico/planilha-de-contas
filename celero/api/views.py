from rest_framework import filters, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from celero.api import models

from . import serializers


class ContabilidadeViewSet(viewsets.ModelViewSet):
    """
    ContabilidadeViewSet:
        - Realiza consultas dos objetos no banco de dados;
        - Implementa os campos de pesquisa e filtros de ordenação por nome e valor;
        - Autenticação e permissão para acesso à API.
    """
    queryset = models.Contabilidade.objects.all()
    serializer_class = serializers.ContabilidadeSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('nome', 'valor')
    ordering_fields = ('nome', 'valor')
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
