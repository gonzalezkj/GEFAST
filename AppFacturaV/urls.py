from django.urls import path
from . import views

urlpatterns = [
    path('', views.facturaventa, name="Facturaventa"),
    path('procesar_venta/', views.procesar_venta, name="procesar_venta"),
]
