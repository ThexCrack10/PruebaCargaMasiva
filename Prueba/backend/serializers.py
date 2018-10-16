from .models import Producto
from rest_framework import serializers

class ProductoSerializers(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Producto
        fields = ('id', 'nombre') 