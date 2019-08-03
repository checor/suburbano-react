from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Linea, Estacion
from .serializers import LineaSerializer, EstacionSerializer
from django.forms.models import model_to_dict


# Create your views here.
class LineaView(ModelViewSet):
    queryset = Linea.objects.all().order_by('id')
    serializer_class = LineaSerializer

class EstacionView(ModelViewSet):
    queryset = Estacion.objects.all().order_by('id')
    serializer_class = EstacionSerializer