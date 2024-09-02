
import requests
from django.shortcuts import render

def lista_tramites(request):
    response = requests.get('https://www.cultura.gob.ar/api/v2.0/tramites/')
    tramites = response.json()
    return render(request, 'tramites/lista_tramites.html', {'tramites': tramites['results']})

