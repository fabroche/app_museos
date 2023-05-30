from django.urls import path, include
from rest_framework import routers

from .Apiviews.estadoConservacionView import EstadoConservacionView

# Routing
routerEstadoConservacion = routers.DefaultRouter()
routerEstadoConservacion.register(r'estadosConservacion', EstadoConservacionView)

urlpatterns = [
    path('api/v1/', include(routerEstadoConservacion.urls)),
]
