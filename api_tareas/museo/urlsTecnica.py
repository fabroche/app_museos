from django.urls import path, include
from rest_framework import routers

from .Apiviews.tecnicaView import TecnicaView

# Routing
routerTecnica = routers.DefaultRouter()
routerTecnica.register(r'tecnicas', TecnicaView)

urlpatterns = [
    path('api/v1/', include(routerTecnica.urls)),
]
