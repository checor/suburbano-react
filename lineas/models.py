from django.db import models

# Create your models here.
class Linea(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)

class Estacion(models.Model):
    nombre = models.CharField(max_length=255)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
    distancia = models.FloatField(default=0)
    estacion_anterior = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)
