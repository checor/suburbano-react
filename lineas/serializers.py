from .models import Linea, Estacion
from rest_framework import serializers

class LineaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Linea
        fields = ('id', 'nombre', 'ubicacion')