from django.urls import path, include
from rest_framework import routers

from .Apiviews.tipoHorarioView import HorarioView

# Routing
routerHorario = routers.DefaultRouter()
routerHorario.register(r'horarios', HorarioView)

urlpatterns = [
    path('api/v1/', include(routerHorario.urls)),
]
