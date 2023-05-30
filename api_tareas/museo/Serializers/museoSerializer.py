from rest_framework import serializers

from ..Models.museo import Museo


class MuseoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museo
        fields = '__all__'
