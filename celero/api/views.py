from rest_framework import generics, filters

from celero.api import models
from . import serializers


class ListContabilidade(generics.ListCreateAPIView):
    queryset = models.Contabilidade.objects.all()
    serializer_class = serializers.ContabilidadeSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('nome', 'valor')
    ordering_fields = ('nome', 'valor')


class DetailContabilidade(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contabilidade.objects.all()
    serializer_class = serializers.ContabilidadeSerializer
