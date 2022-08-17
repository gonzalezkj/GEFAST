from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuentacorriente, name="CC"),
]
