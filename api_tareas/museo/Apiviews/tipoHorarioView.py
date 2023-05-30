from rest_framework import viewsets

from ..Models.tipoHorario import Horario
from ..Serializers.tipoHorarioSerializer import HorarioSerializer


class HorarioView(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    queryset = Horario.objects.all()
