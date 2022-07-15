from django.urls import path
from . import views

urlpatterns = [
    path('', views.registros, name="Registroscompra"),
    path('registroventa', views.registrosventa, name="Registrosventa"),
    path('selectcompra/<id>', views.selectcompra, name="Selectcompra"),
    path('selectcomprapdf/<id>', views.pdf, name="export-pdf"),
]
