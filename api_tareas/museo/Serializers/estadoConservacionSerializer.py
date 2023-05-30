from rest_framework import serializers
from ..Models.estadoConservacion import EstadoConservacion


class EstadoConservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoConservacion
        fields = '__all__'
