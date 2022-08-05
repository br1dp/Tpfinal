from django.contrib import admin
from django.urls import path
from app_1.views import alumnos, cursos, profesores,cursoformulario

from app_1.views import inicio

urlpatterns = [
    path('',inicio,name = 'Inicio'),
    path('cursos/',cursos,name = 'Cursos'),
    path('alumnos/',alumnos,name = 'Alumnos'),
    path('profesores/',profesores,name = 'Profesores'),
    path('cursoformulario/',cursoformulario,name = 'CursoFormulario')
]
