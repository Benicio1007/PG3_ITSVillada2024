from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brewery-data/', views.brewery_data, name='brewery_data'),
]
