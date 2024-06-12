from django.shortcuts import render
import requests

def index(request):
    return render(request, 'brewery_app/index.html')

def brewery_data(request):
    response = requests.get('https://api.openbrewerydb.org/breweries')
    breweries = response.json()
    return render(request, 'brewery_app/brewery_data.html', {'breweries': breweries})
