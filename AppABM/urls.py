from django.urls import path
from . import views

urlpatterns = [
    path('', views.abm, name="Abm"),
    path('abmproveedor/', views.abmproveedor, name="abmproveedor"),
    path('abmarticulo/', views.abmarticulo, name="abmarticulo"),
    path('abmcategoria/', views.abmcategoria, name="abmcategoria"),
    path('agregarcliente/', views.agregar_cliente, name="agregar_cliente"),
    path('modificarcliente/<id>', views.modificar_cliente, name="modificar_cliente"),
    path('agregarproveedor/', views.agregar_proveedor, name="agregar_proveedor"),
    path('modificarproveedor/<id>', views.modificar_proveedor, name="modificar_proveedor"),
    path('agregararticulo/', views.agregar_articulo, name="agregar_articulo"),
    path('modificararticulo/<id>', views.modificar_articulo, name="modificar_articulo"),
    path('agregarcategoria/', views.agregar_categoria, name="agregar_categoria"),
    path('modificarcategoria/<id>', views.modificar_categoria, name="modificar_categoria"),
]
