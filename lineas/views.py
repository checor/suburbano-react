from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 
from .models import Linea, Estacion
from .serializers import LineaSerializer, EstacionSerializer
from django.forms.models import model_to_dict
from rest_framework.pagination import CursorPagination

class CursorSetPagination(CursorPagination):
    ordering = 'id'

# Create your views here.
class LineaView(ModelViewSet):
    #permission_classes = (IsAuthenticated,)    
    queryset = Linea.objects.all().order_by('id')
    serializer_class = LineaSerializer
    pagination_class = CursorSetPagination

class EstacionView(ModelViewSet):
    #permission_classes = (IsAuthenticated,)    
    
    queryset = Estacion.objects.all().order_by('id')
    serializer_class = EstacionSerializer
    pagination_class = CursorSetPagination