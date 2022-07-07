from django.urls import path
from . import views 

app_name="agregarfv"

urlpatterns = [
    path('addfv/<int:factura_id>/', views.addfv, name="addfv"),
    path('clearfv/', views.clearfv, name='clearfv'),
]
