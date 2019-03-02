from rest_framework import serializers
from celero.api import models


class ContabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'nome',
            'valor',
        )
        model = models.Contabilidade
