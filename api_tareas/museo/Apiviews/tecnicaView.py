from rest_framework import viewsets

from ..Models.tecnica import Tecnica
from ..Serializers.tecnicaSerializer import TecnicaSerializer


class TecnicaView(viewsets.ModelViewSet):
    serializer_class = TecnicaSerializer
    queryset = Tecnica.objects.all()
