from django.db import models

from ..Models.exposicion import Exposicion
from ..Models.tipoHorario import Horario


class Museo(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    exposiciones = models.ForeignKey(Exposicion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
