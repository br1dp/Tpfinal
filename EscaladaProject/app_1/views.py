from django.shortcuts import render, redirect
from app_1.forms import AvatarFormulario
from app_1.models import Avatar

from app_1.forms import ProfesoresFormulario
from app_1.models import Profesores

from app_1.forms import AlumnosFormulario
from app_1.models import Alumnos

from django.db.models import Q

from app_1.forms import CursoFormulario, UserEditForm
from app_1.models import Cursos

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def inicio (request):

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render (request,'inicio.html', {"url": avatar.imagen.url})
    except:
         return render (request,'inicio.html')


def cursos(self):

    return render(self,"cursos.html")


def alumnos(self):

    return render(self,"alumnos.html")


def profesores(self):

    return render(self,"profesores.html")

@login_required
@staff_member_required (login_url = '/app_1/')
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



def tabla_cursos(request):

    lista = Cursos.objects.all()
    return render (request, 'tablacursos.html',{"tabla_cursos": lista})


@login_required
@staff_member_required (login_url = '/app_1/')
def edita_cursos(request, id):
    
    print("method:",request.method)
    print("request:",request.POST)

    curso = Cursos.objects.get(id=id)

    if request.method == "POST":

        cursoformulario = CursoFormulario(request.POST)

        if cursoformulario.is_valid():
            
            data = cursoformulario.cleaned_data
        
            curso.nivel = data["nivel"]
            curso.dia = data["dia"]
            curso.horario = data["horario"]
            curso.profesor = data["profesor"]

        curso.save()

        return render(request,'cursos.html')

    else:

        cursoformulario = CursoFormulario(initial = {
            "nivel": curso.nivel,
            "dia": curso.dia,
            "horario": curso.horario,
            "profesor": curso.profesor,
        })
    
    return render(request,'editarcursos.html',{'cursoformulario':cursoformulario, 'id':curso.id})

@staff_member_required(login_url = '/app_1/')  
@login_required
def elimina_cursos(request, id):

    print("method:",request.method)
    print("request:",request.POST)

    curso = Cursos.objects.get(id=id)

    if request.method == "POST":

        return render(request,'eliminarcurso.html', {'curso':curso})
        
    curso.delete()

    return redirect ('TablaCursos')

@login_required
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

@login_required
def profesoresformulario(request):

    print("method:",request.method)
    print("request:",request.POST)

    if request.method == "POST":

        profesoresformulario = ProfesoresFormulario(request.POST)

        if profesoresformulario.is_valid():
            
            data = profesoresformulario.cleaned_data
        
        profesor = Profesores(nombre = data["nombre"],apellido = data["apellido"], email = data ["email"])

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


def loginView(request):

    if request.method == 'POST':

        loginFormulario = AuthenticationForm(request, data=request.POST)

        if loginFormulario.is_valid(): 
            
            data = loginFormulario.cleaned_data 
            
            usuario = data["username"]

            psw = data["password"]
            
            user = authenticate(username = usuario, password = psw)
            
            if user:

              login(request, user)

              return render(request, 'padre.html', {"mensaje": f'Bienvenido "{usuario}", ha iniciado sesi??n correctamente'})
             
            else:
                
              return render(request, 'padre.html', {"mensaje": f'ERROR: Los datos ingresados no son v??lidos'})

        return render (request, 'padre.html', {"mensaje": f'ERROR: Los datos ingresados no son v??lidos'})
    
    else: 

       loginFormulario = AuthenticationForm()

    return render (request, 'login.html', {"loginFormulario": loginFormulario})




def register(request):

    if request.method == 'POST':

        formRegister = UserCreationForm(request.POST)

        if formRegister.is_valid():

         username = formRegister.cleaned_data["username"]

         formRegister.save()

         return render(request, 'padre.html', {"mensaje": f'El usuario "{username}", ha sido creado'})
    
    else: 
        formRegister = UserCreationForm()

    return render(request, "registro.html",  {"formRegister": formRegister})



@login_required
def editar_perfil(request):

    print('method:', request.method)
    print('post:', request.method)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid(): 
            
            data = miFormulario.cleaned_data 
            
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            
            usuario.save()
            
            return render (request, 'inicio.html', {"mensaje": 'Se guardaron los cambios'})
    
    else: 

       miFormulario = UserEditForm(instance = request.user)

    return render (request, 'editarPerfil.html', {"miFormulario": miFormulario})

@login_required
def agregar_avatar(request):

    if request.method == "POST":

        avatarFormulario = AvatarFormulario(request.POST, request.FILES)

        if avatarFormulario.is_valid():
            
            data = avatarFormulario.cleaned_data
            
            avatar = Avatar(user=request.user , imagen=data['imagen'])
            
            avatar.save()

        return render(request,'inicio.html', {"mensaje": "Avatar cargado.."})

    else:

        avatarFormulario = AvatarFormulario()
    
    return render(request,'cargarAvatar.html',{'avatarFormulario':avatarFormulario})


def tabla_alumnos(request):

    lista = Alumnos.objects.all()
    return render (request, 'tablaalumnos.html',{"tabla_alumnos": lista})

@login_required
def edita_alumno(request, id):
    
    print("method:",request.method)
    print("request:",request.POST)

    alumno = Alumnos.objects.get(id=id)

    if request.method == "POST":

        alumnoformulario = AlumnosFormulario(request.POST)

        if alumnoformulario.is_valid():
            
            data = alumnoformulario.cleaned_data
        
            alumno.nombre = data["nombre"]
            alumno.apellido = data["apellido"]
            alumno.edad = data["edad"]
            alumno.email = data["email"]

        alumno.save()

        return render(request,'alumnos.html')

    else:

        alumnoformulario = AlumnosFormulario(initial = {
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "edad": alumno.edad,
            "email": alumno.email,
        })
    
    return render(request,'editaralumno.html',{'alumnoformulario':alumnoformulario, 'id':alumno.id})

@login_required
def elimina_alumno(request, id):


    print("method:",request.method)
    print("request:",request.POST)

    alumno = Alumnos.objects.get(id=id)

    if request.method == "POST":

        return render(request,'eliminaralumno.html', {'alumno':alumno})
        
    alumno.delete()

    return redirect ('TablaAlumnos')

def tabla_profesores(request):

    lista = Profesores.objects.all()
    return render (request, 'tablaprofesores.html',{"tabla_profesores": lista})


@login_required
def edita_profe(request, id):
    
    print("method:",request.method)
    print("request:",request.POST)

    profesor = Profesores.objects.get(id=id)

    if request.method == "POST":

        profesorformulario = ProfesoresFormulario(request.POST)

        if profesorformulario.is_valid():
            
            data = profesorformulario.cleaned_data
        
            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]

        profesor.save()

        return render(request,'profesores.html')

    else:

        profesorformulario = ProfesoresFormulario(initial = {
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
        })
    
    return render(request,'editarprofesor.html',{'profesorformulario':profesorformulario, 'id':profesor.id})
 
@login_required
def elimina_profesor(request, id):

    print("method:",request.method)
    print("request:",request.POST)

    profesor = Profesores.objects.get(id=id)

    if request.method == "POST":

        return render(request,'eliminarprofesor.html', {'profesor':profesor})
        
    profesor.delete()


    return redirect ('TablaProfesores')

    

