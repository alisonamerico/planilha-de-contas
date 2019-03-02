from rest_framework import generics

from celero.api import models
from . import serializers


class ListContabilidade(generics.ListCreateAPIView):
    queryset = models.Contabilidade.objects.all()
    serializer_class = serializers.ContabilidadeSerializer


class DetailContabilidade(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contabilidade.objects.all()
    serializer_class = serializers.ContabilidadeSerializer
