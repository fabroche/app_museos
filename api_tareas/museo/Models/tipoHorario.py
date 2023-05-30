from django.db import models


class Horario(models.Model):
    tipo = models.CharField(max_length=255)
    hora_apertura = models.DateTimeField()
    hora_clausura = models.DateTimeField()

    def __str__(self):
        return self.tipo
