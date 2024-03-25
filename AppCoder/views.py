from django.shortcuts import render
#Importando el modelo dar de alta uno nuevo importando la clase curso
from AppCoder.models import Curso
from django.http import HttpResponse


# Create your views here.
#4 Definir las views

#Responder en la platilla renderizada
def inicio(request):
    return render(request, "padre.html")

def alta_curso(request, nombre):
    #contructor de la clase, un objeto mas lo que hereda
    curso = Curso(nombre=nombre, camada= 234512)
    curso.save()
    
    #Dar de alta los registros en la base de datos para insertarlos desde la interfaz
    texto=f"Se guardo en la DB el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)