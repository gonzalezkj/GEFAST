from rest_framework.viewsets import ModelViewSet
from AppArticulos.models import Articulo
from AppArticulos.api.serializers import ArticuloSerializer

class ArticuloApiViewSet(ModelViewSet):
    serializer_class = ArticuloSerializer
    queryset = Articulo.objects.all()