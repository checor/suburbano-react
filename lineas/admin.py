from django.contrib import admin
from .models import Linea, Estacion

# Register your models here.
admin.site.register([Linea, Estacion])