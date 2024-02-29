from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'proveedor',
            'imagen'
        ]
        extra_kwargs = {
            'imagen': {'read_only': True},
            'descripcion': {'required': False},
            'id': {'read_only': True},
        }