"""
URLs del proyecto. Aquí solo se "incluyen" (include) las rutas propias de
cada app — las rutas reales de la página de inicio viven en examenes/urls.py.
Así se ve la relación proyecto -> app que pide el Paso 8 de la pauta.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('examenes.urls')),  # delega la ruta raíz "/" a la app
]
