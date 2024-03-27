from django.urls import path
from . import views

urlpatterns= [
    path("", views.inicio),
    path("ver_cursos", views.ver_cursos),
    path("alta_curso/<nombre>", views.alta_curso)
    
]