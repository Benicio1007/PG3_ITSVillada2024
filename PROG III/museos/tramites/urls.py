from django.urls import path
from . import views  

urlpatterns = [
    path('', views.lista_tramites, name='lista_tramites'), 
]

