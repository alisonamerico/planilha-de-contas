from rest_framework import serializers
from celero.api import models


"""
ContabilidadeSerializer - Irá fazer a tradução dos objetos implementados no Model Contabilidade
para visualização dos mesmos no form do DRF.
"""


class ContabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'controle',
            'nome',
            'valor',
        )
        model = models.Contabilidade
