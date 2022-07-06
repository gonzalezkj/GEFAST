from django.urls import path
from . import views 

app_name="agregarprov"

urlpatterns = [
    path('addprov/<int:prov_id>/', views.addprov, name="addprov"),
    path('removeprov/<int:prov_id>/', views.removeprov, name="removeprov"),
    path('clearprov/', views.clearprov, name='clearprov'),
]
