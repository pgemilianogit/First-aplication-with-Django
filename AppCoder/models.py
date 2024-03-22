from django.db import models

# Create your models here.

#Crear clase modulo Heredando de la clase padre para funcionalidad
class Curso(models.Model):
    
    #1. Estructura de datos donde el modelo es una clase y como se almacenaran los datos en la DB (SQL)
    #2. Clase18 Settings.py y en ISTALLED_APP
    nombre= models.CharField(max_length=40)
    camada=models.IntegerField()