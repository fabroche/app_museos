from django.db import models

from ..Models.artista import Artista
from ..Models.estadoConservacion import EstadoConservacion

from ..Models.tecnica import Tecnica
from ..Models.exposicion import Exposicion


class Obra(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    historia = models.TextField(blank=True)
    estado_conservacion = models.ForeignKey(EstadoConservacion, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    exposicion = models.ForeignKey(Exposicion, on_delete=models.CASCADE, null=True)
    tecnica_utilizada = models.ForeignKey(Tecnica, on_delete=models.CASCADE)
    fecha_creada = models.DateTimeField()

    def __str__(self):
        return self.nombre
