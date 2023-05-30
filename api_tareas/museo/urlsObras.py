from django.urls import path, include
from rest_framework import routers

from .Apiviews.obraView import ObraView

# Routing
routerObras = routers.DefaultRouter()
routerObras.register(r'obras', ObraView)

urlpatterns = [
    path('api/v1/', include(routerObras.urls)),
]
