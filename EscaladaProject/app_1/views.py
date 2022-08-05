from django.shortcuts import render

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
        
        curso = Cursos(nivel = data["Nivel"],horario = data["Horario"],profesor = data ["Profesor"])

        curso.save()

        return render(request,'lsitacursos.html')

    else:

        cursoformulario = CursoFormulario()
    
    return render(request,'cursoformulario.html',{'cursoformulario':cursoformulario})