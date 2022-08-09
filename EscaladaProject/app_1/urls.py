from django.contrib import admin
from django.urls import path
from app_1.views import buscarcursos

from app_1.views import busquedacursos
from app_1.views import alumnosformulario
from app_1.views import alumnos, cursos, profesores,cursoformulario,profesoresformulario
from app_1.views import inicio

urlpatterns = [
    path('',inicio,name = 'Inicio'),
    path('cursos/',cursos,name = 'Cursos'),
    path('alumnos/',alumnos,name = 'Alumnos'),
    path('profesores/',profesores,name = 'Profesores'),
    path('cursoformulario/',cursoformulario,name = 'CursoFormulario'),
    path('busquedacursos/',buscarcursos,name = 'BuscarCursos'),
    path('alumnosformulario/',alumnosformulario,name = 'AlumnosFormulario'),
    path('busquedaalumnos/',inicio,name = 'ListaAlumnos'),
    path('profesoresformulario/',profesoresformulario,name = 'ProfesoresFormulario'),
]
