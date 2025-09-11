from django.urls import path
from .views import AddVeiculo, UpdateVeiculo, DeleteVeiculo

app_name = 'mainApp'

urlpatterns = [
    path("", views.AddVeiculo, name=''),
    
]