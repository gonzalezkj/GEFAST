from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from AppArticulos.models import Articulo

class ArticuloSerializer(ModelSerializer):

    class Meta:
        model = Articulo
        fields = ['id_articulo','cantidad','nombre', 'precio', 'disponibilidad', 'categoria']
        
    def to_representation(self, instance):
        return {
            'id_articulo': instance.id_articulo,
            'cantidad': instance.cantidad,
            'nombre': instance.nombre,
            'precio': instance.precio,
            'categoria': instance.categoria.nombre,
        }