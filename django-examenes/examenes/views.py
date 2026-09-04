"""
Vistas de la app "examenes".

Para esta primera evaluación solo existe la vista de bienvenida: todavía no
hay modelos ni persistencia (eso llega en la próxima evaluación), pero la
vista ya usa variables, una estructura de datos (diccionario + lista) y una
estructura de control simple, para demostrar el manejo básico del lenguaje.
"""
from datetime import datetime
from django.shortcuts import render

# Información del proyecto: variables y estructuras de datos usadas en la vista.
PROYECTO = {
    'nombre': 'Gestión de Exámenes',
    'alumno': 'Luis Matias Núñez Nain',
    'curso': 'Programación Backend',
    'descripcion': (
        'Plataforma para que docentes creen exámenes con preguntas y '
        'alternativas, y estudiantes matriculados los rindan dentro de un '
        'periodo habilitado, con calificación automática de sus respuestas.'
    ),
}

MODULOS_PLANIFICADOS = [
    'Gestión de cursos y matrículas',
    'Creación de exámenes y preguntas',
    'Rendición de exámenes por parte de estudiantes',
    'Calificación automática y reportes de resultados',
]


def obtener_saludo():
    """Devuelve un saludo distinto según la hora del día (estructura de control)."""
    hora_actual = datetime.now().hour
    if hora_actual < 12:
        return 'Buenos días'
    elif hora_actual < 19:
        return 'Buenas tardes'
    else:
        return 'Buenas noches'


def inicio(request):
    """Página de bienvenida del proyecto (reemplaza la página default de Django)."""
    contexto = {
        'saludo': obtener_saludo(),
        'proyecto': PROYECTO,
        'modulos': MODULOS_PLANIFICADOS,
        'total_modulos': len(MODULOS_PLANIFICADOS),
    }
    return render(request, 'examenes/inicio.html', contexto)
