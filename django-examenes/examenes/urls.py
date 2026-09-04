"""
Rutas propias de la app "examenes". El proyecto (config/urls.py) delega
la ruta raíz aquí mediante include('examenes.urls').
"""
from django.urls import path
from . import views

app_name = 'examenes'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
