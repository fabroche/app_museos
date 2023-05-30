from rest_framework import serializers

from ..Models.obra import Obra


class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'
