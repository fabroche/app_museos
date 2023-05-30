from rest_framework import viewsets

from ..Models.artista import Artista
from ..Serializers.artistaSerializer import ArtistaSerializer


class ArtistaView(viewsets.ModelViewSet):
    serializer_class = ArtistaSerializer
    queryset = Artista.objects.all()
