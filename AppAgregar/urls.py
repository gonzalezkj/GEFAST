from django.urls import path
from . import views 

app_name="agregar"

urlpatterns = [
    path('add/<int:articulo_id>/', views.add, name="add"),
    path('remove/<int:articulo_id>/', views.remove, name="remove"),
    path('decrement/<int:articulo_id>/', views.decrement, name="decrement"),
    path('clear/', views.clear, name='clear'),
]
