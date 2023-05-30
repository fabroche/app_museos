from rest_framework import viewsets

from ..Models.estadoConservacion import EstadoConservacion
from ..Serializers.estadoConservacionSerializer import EstadoConservacionSerializer


class EstadoConservacionView(viewsets.ModelViewSet):
    serializer_class = EstadoConservacionSerializer
    queryset = EstadoConservacion.objects.all()
