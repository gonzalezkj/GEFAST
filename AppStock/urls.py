from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock, name="Stock"),
    path('precio/', views.precio, name="Precio"),
    path('agregar/', views.agregar_articulo, name="agregar_articulo"),
]
