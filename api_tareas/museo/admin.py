from django.contrib import admin

from .Models.exposicion import Exposicion
from .Models.museo import Museo
from .Models.tipoHorario import Horario

from .Models.artista import Artista
from .Models.estadoConservacion import EstadoConservacion
from .Models.exposicion import Exposicion
from .Models.obra import Obra
from .Models.tecnica import Tecnica

# Museo
admin.site.register(Museo)
admin.site.register(Horario)
admin.site.register(Exposicion)

# Obras
admin.site.register(Obra)
admin.site.register(Artista)
admin.site.register(EstadoConservacion)
admin.site.register(Tecnica)
