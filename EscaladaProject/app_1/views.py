from django.shortcuts import render

from app_1.forms import ProfesoresFormulario
from app_1.models import Profesores

from app_1.forms import AlumnosFormulario
from app_1.models import Alumnos

from django.db.models import Q

from app_1.forms import CursoFormulario
from app_1.models import Cursos

def inicio (self):

    return render (self,'inicio.html')

def cursos(self):

    return render(self,"cursos.html")

def alumnos(self):

    return render(self,"alumnos.html")

def profesores(self):

    return render(self,"profesores.html")

def cursoformulario(request):

    print("method:",request.method)
    print("request:",request.POST)

    if request.method == "POST":

        cursoformulario = CursoFormulario(request.POST)

        if cursoformulario.is_valid():
            
            data = cursoformulario.cleaned_data
        
        curso = Cursos(nivel = data["nivel"], dia = data["dia"], horario = data["horario"],profesor = data ["profesor"])

        curso.save()

        return render(request,'cursos.html')

    else:

        cursoformulario = CursoFormulario()
    
    return render(request,'cursoformulario.html',{'cursoformulario':cursoformulario})


def alumnosformulario(request):

    print("method:",request.method)
    print("request:",request.POST)

    if request.method == "POST":

        alumnosformulario = AlumnosFormulario(request.POST)

        if alumnosformulario.is_valid():
            
            data = alumnosformulario.cleaned_data
        
        alumno = Alumnos(nombre = data["nombre"],apellido = data["apellido"],edad = data ["edad"],email = data ["email"])

        alumno.save()

        return render(request,'alumnos.html')

    else:

        alumnosformulario = AlumnosFormulario()
    
    return render(request,'alumnosformulario.html',{'alumnosformulario':alumnosformulario})

def profesoresformulario(request):

    print("method:",request.method)
    print("request:",request.POST)

    if request.method == "POST":

        profesoresformulario = ProfesoresFormulario(request.POST)

        if profesoresformulario.is_valid():
            
            data = profesoresformulario.cleaned_data
        
        profesor = Profesores(nombre = data["nombre"],apellido = data["apellido"], cursos = data ["curso"],email = data ["email"])

        profesor.save()

        return render(request,'profesores.html')

    else:

        profesoresformulario = ProfesoresFormulario()
    
    return render(request,'profesoresformulario.html',{'profesoresformulario':profesoresformulario})


def busquedacursos(request):

    return render(request,'busquedacursos.html')

def resultadocursos(request):

    if request.method == "GET":
        
        nivel = request.GET['nivel']

        if nivel != "":
          niveles = Cursos.objects.filter( Q(nivel__icontains = nivel) | Q (dia__icontains = nivel) | Q (horario__icontains = nivel) | Q(profesor__icontains = nivel) ).values()

          return render(request,'resultadocurso.html',{'niveles':niveles})

    niveles = Cursos.objects.all()
    return render(request, "alumnos.html",{"niveles": niveles})

def busquedaalumnos(request):

    return render(request,'busquedaalumnos.html')

def resultadoalumnos(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']

        nombres = Alumnos.objects.filter(nombre__icontains = nombre)

        return render (request,'resultadoalumnos.html',{'nombres':nombres,'nombre':nombre})

def busquedaprofesores(request):

    return render(request,'busquedaprofesores.html')

def resultadoprofesores(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']

        nombres = Profesores.objects.filter(nombre__icontains = nombre)

        return render (request,'resultadoprofesores.html',{'nombres':nombres,'nombre':nombre})

def tabla_cursos(request):

    lista = Cursos.objects.all()
    return render (request, 'tablacursos.html',{"tabla_cursos": lista})
