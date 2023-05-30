from rest_framework import serializers

from ..Models.tecnica import Tecnica


class TecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnica
        fields = '__all__'
