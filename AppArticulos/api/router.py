from rest_framework.routers import DefaultRouter
from AppArticulos.api.views import ArticuloApiViewSet

router_articulos = DefaultRouter()

router_articulos.register(prefix='articulo', basename='articulo', viewset=ArticuloApiViewSet)