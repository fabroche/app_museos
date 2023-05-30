from django.urls import path, include
from rest_framework import routers

from .Apiviews.exposicionView import ExposicionView

# Routing
routerExposiciones = routers.DefaultRouter()
routerExposiciones.register(r'exposiciones', ExposicionView)

urlpatterns = [
    path('api/v1/', include(routerExposiciones.urls)),
]
