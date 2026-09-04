# Gestión de Exámenes — Backend (Python + Django)

**Evaluación 1** · Repositorio GitHub, ambiente virtual, núcleo Django y aplicación inicial
Alumno: **Luis Matias Núñez Nain**

Plataforma para que docentes creen exámenes con preguntas y estudiantes matriculados los rindan. **Esta primera entrega solo cubre la base técnica**: repositorio, ambiente virtual, proyecto Django, una app propia (`examenes`), rutas propias, página de bienvenida y página 404 personalizada. El modelo de datos y el CRUD llegan en la siguiente evaluación.

---

## 1. Preparar el repositorio (una sola vez)

```bash
mkdir gestion-examenes-django && cd gestion-examenes-django
git init
```

Copia todos los archivos de este proyecto dentro de esa carpeta (o descomprímelos ahí directamente).

## 2. Crear y activar el ambiente virtual

```bash
python -m venv .venv

# Activar (elige según tu sistema):
source .venv/bin/activate        # Linux / Mac
.venv\Scripts\activate           # Windows (cmd)
.venv\Scripts\Activate.ps1       # Windows (PowerShell)
```

Vas a ver `(.venv)` al inicio de tu terminal — eso es lo que el profesor pidió que fuera "visible y comprobable".

## 3. Instalar Django y dependencias

```bash
pip install -r requirements.txt
```

## 4. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` — debe aparecer la **página de bienvenida del proyecto** (no la página por defecto de Django).

## 5. Probar la página 404 personalizada

Django solo usa tu `templates/404.html` cuando `DEBUG = False`. Para demostrarlo en la evaluación:

1. Abre `config/settings.py`.
2. Cambia `DEBUG = True` por `DEBUG = False`.
3. Guarda y vuelve a correr `python manage.py runserver`.
4. Entra a cualquier URL que no exista, por ejemplo `http://127.0.0.1:8000/no-existe`.
5. Debe aparecer tu página 404 personalizada (no la técnica de Django).
6. Cuando termines de mostrarla, vuelve a dejar `DEBUG = True` para seguir desarrollando.

> Esto es normal en Django, no un error tuyo — con `DEBUG=True` siempre se ve la página técnica de error para poder depurar; con `DEBUG=False` se usa tu plantilla personalizada.

## 6. Subir a GitHub

```bash
git add .
git commit -m "Inicializa proyecto Django y estructura base"
# ... ve haciendo commits por avance, no todo junto, por ejemplo:
git commit -m "Crea app examenes y la registra en INSTALLED_APPS"
git commit -m "Agrega vista y template de bienvenida"
git commit -m "Agrega template 404 personalizado"

git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git push -u origin main
```

Verifica que **NO** se haya subido la carpeta `.venv/` ni `db.sqlite3` (el `.gitignore` ya los excluye).

---

## Estructura del proyecto

```
gestion-examenes-django/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── 404.html                  ← página 404 personalizada (a nivel de proyecto)
├── config/                       ← núcleo del proyecto Django
│   ├── settings.py
│   ├── urls.py                   ← incluye las rutas de la app "examenes"
│   ├── wsgi.py
│   └── asgi.py
└── examenes/                     ← app propia del proyecto
    ├── views.py                  ← vista de bienvenida (inicio)
    ├── urls.py                   ← ruta "" → views.inicio
    ├── models.py                 ← vacío por ahora (próxima evaluación)
    └── templates/examenes/
        └── inicio.html           ← template de la página de bienvenida
```

## Cómo se relacionan las rutas (proyecto → app)

1. `config/urls.py` es el punto de entrada: `path('', include('examenes.urls'))` delega **toda la raíz** a la app.
2. `examenes/urls.py` define la ruta real: `path('', views.inicio, name='inicio')`.
3. `examenes/views.py` contiene la función `inicio(request)`, que arma el contexto (variables, diccionario `PROYECTO`, lista `MODULOS_PLANIFICADOS`) y renderiza `examenes/templates/examenes/inicio.html`.

## Posibles respuestas rápidas para las 4 preguntas del profesor

- **Ambiente virtual**: aísla las dependencias de este proyecto del resto del sistema; se activa con `source .venv/bin/activate` y se nota porque aparece `(.venv)` en la terminal.
- **Rutas**: el proyecto (`config/urls.py`) delega con `include()` a las rutas de la app (`examenes/urls.py`); así el proyecto puede tener muchas apps, cada una con sus propias rutas.
- **Vistas**: una vista es una función que recibe `request` y devuelve una respuesta (`render` con un template + contexto). `inicio()` es la vista de bienvenida.
- **Dependencias**: `requirements.txt` solo tiene `Django`; se instala con `pip install -r requirements.txt` dentro del ambiente virtual activado.
- **Variables/estructuras**: `PROYECTO` es un diccionario con los datos del proyecto; `MODULOS_PLANIFICADOS` es una lista; `obtener_saludo()` usa una estructura de control (`if/elif/else`) según la hora del día.
