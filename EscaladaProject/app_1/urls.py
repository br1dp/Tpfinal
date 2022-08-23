from django.contrib import admin
from django.urls import path
from .views import edita_alumno, edita_cursos, edita_profe, elimina_alumno, elimina_profesor,loginView, register, tabla_alumnos, tabla_profesores

from app_1.views import resultadoprofesores
from app_1.views import busquedaprofesores
from app_1.views import resultadoalumnos
from app_1.views import busquedaalumnos
from app_1.views import resultadocursos
from app_1.views import busquedacursos
from app_1.views import alumnosformulario
from app_1.views import tabla_cursos
from app_1.views import alumnos, cursos, profesores, cursoformulario, profesoresformulario, elimina_cursos
from app_1.views import inicio
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',inicio,name = 'Inicio'),
    path('login/',loginView, name = 'Login'),
    path('registro/',register, name = 'Registro'),
    path('logout/', LogoutView.as_view(template_name ="logout.html"), name = 'Logout'),

    path('cursos/',cursos,name = 'Cursos'),
    path('cursoformulario/',cursoformulario,name = 'CursoFormulario'),
    path('busquedacursos/',busquedacursos,  name = 'BuscarCursos'),
    path('tablacursos/',tabla_cursos,  name = 'TablaCursos'),

    path('resultadocursos/',resultadocursos, name = 'ResultadoCursos'),
    path('editarcursos/<int:id>',edita_cursos , name = 'EditarCursos'),
    path('eliminacursos/<int:id>',elimina_cursos , name = 'EliminaCursos'),

    path('alumnos/',alumnos,name = 'Alumnos'),
    path('alumnosformulario/',alumnosformulario,name = 'AlumnosFormulario'),
    path('busquedaalumnos/',busquedaalumnos,name = 'BusquedaAlumnos'),
    path('resultadoalumnos/',resultadoalumnos,name = 'ResultadoAlumnos'),
    path('tablaalumnos/',tabla_alumnos,  name = 'TablaAlumnos'),
    path('editaralumnos/<int:id>',edita_alumno , name = 'EditaAlumnos'),
    path('eliminaalumnos/<int:id>',elimina_alumno , name = 'EliminaAlumnos'),

    path('profesores/',profesores,name = 'Profesores'),
    path('profesoresformulario/',profesoresformulario,name = 'ProfesoresFormulario'),
    path('busquedaprofesores/',busquedaprofesores,name = 'BusquedaProfesores'),
    path('resultadoprofesores/',resultadoprofesores,name = 'ResultadoProfesores'),
    path('tablaprofesores/',tabla_profesores,  name = 'TablaProfesores'),
    path('editarprofesores/<int:id>',edita_profe , name = 'EditaProfesores'),
    path('eliminaprofesores/<int:id>',elimina_profesor , name = 'EliminaProfesores'),

    ]
