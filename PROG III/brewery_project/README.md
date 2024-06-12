# Proyecto de Cervecerías

Este proyecto de Django muestra información sobre cervecerías usando la API de [Open Brewery DB](https://www.openbrewerydb.org/).

## Requisitos

- Python 3.10 o superior
- Django 5.0.6
- requests 2.26.0
- Bootstrap 4.5.2 (para el diseño del frontend)

## Instalación

1. Clona el repositorio a tu compu:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd brewery_project
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  
    ```

3. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Ve al directorio del proyecto:

    ```bash
    cd brewery_project
    ```

2. Configura las migraciones y la base de datos:

    ```bash
    python manage.py migrate
    ```

3. Arranca el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Uso

1. Abre tu navegador web y ve a `http://127.0.0.1:8000/`.
2. En la página principal, haz clic en el botón "Ver datos de la cervecería" para ver la info sobre las cervecerías.

## Estructura del Proyecto

- `brewery_project/`: Configuración principal del proyecto Django.
  - `settings.py`: Configuración del proyecto.
  - `urls.py`: Rutas principales del proyecto.
  - `wsgi.py`: Configuración del servidor WSGI.

- `brewery_app/`: Lógica de la aplicación.
  - `views.py`: Vista para obtener datos de la API y renderizar la plantilla.
  - `templates/`: Plantillas HTML.
    - `index.html`: Página principal.
    - `brewery_data.html`: Muestra la información de las cervecerías.

## API Utilizada

### Open Brewery DB

Usamos la API de [Open Brewery DB](https://www.openbrewerydb.org/) para obtener info sobre cervecerías.

### Ejemplo de Uso de la API

En `views.py`, usamos la librería `requests` para hacer una solicitud GET a la API y obtener los datos de las cervecerías:

```python
import requests
from django.shortcuts import render

def brewery_data(request):
    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(url)
    breweries = response.json()
    return render(request, 'brewery_data.html', {'breweries': breweries})
