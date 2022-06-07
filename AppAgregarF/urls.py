from django.urls import path
from . import views 

app_name="agregarf"

urlpatterns = [
    path('add/<int:factura_id>/', views.addf, name="addf"),
    path('clear/', views.clearf, name='clearf'),
]
