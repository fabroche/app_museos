from django.urls import path, include
from rest_framework import routers

from .Apiviews.museoView import MuseoView

# Routing
routerMuseos = routers.DefaultRouter()
routerMuseos.register(r'museos', MuseoView)


urlpatterns = [
    path('api/v1/', include(routerMuseos.urls)),
]
