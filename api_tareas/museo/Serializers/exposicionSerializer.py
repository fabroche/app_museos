from rest_framework import serializers

from ..Models.exposicion import Exposicion


class ExposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposicion
        fields = '__all__'
