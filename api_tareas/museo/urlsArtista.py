from django.urls import path, include
from rest_framework import routers

from .Apiviews.artistaView import ArtistaView

# Routing
routerArtistas = routers.DefaultRouter()
routerArtistas.register(r'artistas', ArtistaView)

urlpatterns = [
    path('api/v1/', include(routerArtistas.urls)),
]
