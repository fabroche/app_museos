from rest_framework import viewsets

from ..Models.obra import Obra
from ..Serializers.obraSerializer import ObraSerializer


class ObraView(viewsets.ModelViewSet):
    serializer_class = ObraSerializer
    queryset = Obra.objects.all()
