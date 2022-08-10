from django.contrib import admin
from django.urls import path


from app_1.views import resultadoprofesores
from app_1.views import busquedaprofesores
from app_1.views import resultadoalumnos
from app_1.views import busquedaalumnos
from app_1.views import resultadocursos
from app_1.views import busquedacursos
from app_1.views import alumnosformulario
from app_1.views import alumnos, cursos, profesores,cursoformulario,profesoresformulario
from app_1.views import inicio

urlpatterns = [
    path('',inicio,name = 'Inicio'),
    path('cursos/',cursos,name = 'Cursos'),
    path('cursoformulario/',cursoformulario,name = 'CursoFormulario'),
    path('busquedacursos/',busquedacursos,name = 'BuscarCursos'),
    path('resultadocursos/',resultadocursos,name = 'ResultadoCursos'),

    path('alumnos/',alumnos,name = 'Alumnos'),
    path('alumnosformulario/',alumnosformulario,name = 'AlumnosFormulario'),
    path('busquedaalumnos/',busquedaalumnos,name = 'BusquedaAlumnos'),
    path('resultadoalumnos/',resultadoalumnos,name = 'ResultadoAlumnos'),

    path('profesores/',profesores,name = 'Profesores'),
    path('profesoresformulario/',profesoresformulario,name = 'ProfesoresFormulario'),
    path('busquedaprofesores/',busquedaprofesores,name = 'BusquedaProfesores'),
    path('resultadoprofesores/',resultadoprofesores,name = 'ResultadoProfesores'),
    ]
