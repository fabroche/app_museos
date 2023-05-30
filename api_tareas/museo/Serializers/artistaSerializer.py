from rest_framework import serializers

from ..Models.artista import Artista


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'
