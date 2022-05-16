from django.urls import path
from . import views

urlpatterns = [
    path('', views.abm, name="Abm"),
    path('agregar/', views.agregar_cliente, name="agregar_cliente"),
]
