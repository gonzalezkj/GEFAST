from django.urls import path
from AppBase import views

urlpatterns = [
    path('', views.home, name="Home"),
]
