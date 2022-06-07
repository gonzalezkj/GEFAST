from django.urls import path
from . import views

urlpatterns = [
    path('', views.factura, name="Factura"),
    path('procesarventa/', views.procesar_venta, name="procesar_venta"),
]
