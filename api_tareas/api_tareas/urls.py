from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# para Swagger
from rest_framework.schemas import get_schema_view

# Swagger Docs
swaggerUi_schema = get_schema_view(
    title='SwaggerUI ApiMuseo',
    description='Guide for the API Task',
    version='v1.0.0',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('task/', include('task.urls')),
    path('museo/', include('museo.urls')),
    path('exposicion/', include('museo.urlsExposiciones')),
    path('horario/', include('museo.urlsTipoHorario')),
    path('artista/', include('museo.urlsArtista')),
    path('estado-conservacion/', include('museo.urlsEstadoConservacion')),
    path('tecnica/', include('museo.urlsTecnica')),

    path('obra/', include('museo.urlsObras')),

    # End Point para construir el schema de configuracion del Swagger
    path('schema/', swaggerUi_schema, name="schema-apiTask"),

    # End Point para visitar la Documentacion de la Api
    path('api-museo/docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'schema-apiTask'}
    ), name='swagger-ui'),
]
