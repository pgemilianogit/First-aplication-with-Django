from django.urls import path
from . import views

urlpatterns= [
    path("alta_curso/<nombre>", views.alta_curso)
    
]