from django.urls import path
from . import views 

app_name="agregarcli"

urlpatterns = [
    path('addcli/<int:cliente_id>/', views.addcli, name="addcli"),
    path('removecli/<int:cliente_id>/', views.removecli, name="removecli"),
    path('clearcli/', views.clearcli, name='clearcli'),
]
