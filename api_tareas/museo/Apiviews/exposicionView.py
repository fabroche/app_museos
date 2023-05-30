from rest_framework import viewsets

from ..Models.exposicion import Exposicion
from ..Serializers.exposicionSerializer import ExposicionSerializer


class ExposicionView(viewsets.ModelViewSet):
    serializer_class = ExposicionSerializer
    queryset = Exposicion.objects.all()
