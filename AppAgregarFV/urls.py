from django.urls import path
from . import views 

app_name="agregarfv"

urlpatterns = [
    path('add/<int:factura_id>/', views.addfv, name="addfv"),
    path('clear/', views.clearfv, name='clearfv'),
]
