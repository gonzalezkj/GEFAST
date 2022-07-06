from django.urls import path
from . import views

urlpatterns = [
    path('', views.factura, name="Factura"),
    path('procesar_compra/', views.procesar_compra, name="procesar_compra"),
]
