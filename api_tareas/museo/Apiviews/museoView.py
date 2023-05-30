from rest_framework import viewsets

from ..Models.museo import Museo
from ..Serializers.museoSerializer import MuseoSerializer


class MuseoView(viewsets.ModelViewSet):
    serializer_class = MuseoSerializer
    queryset = Museo.objects.all()
