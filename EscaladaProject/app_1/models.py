from distutils.command.upload import upload
from django.db import models

from django.contrib.auth.models import User


class Cursos(models.Model):

    nivel = models.CharField(max_length=20)

    dia = models.CharField(max_length=20)
        
    horario = models.CharField(max_length=20)

    profesor = models.CharField( max_length=50)

    def __str__(self) -> str:
        return f"Niveles: {self.nivel}  / Día: {self.dia}  Horarios: {self.horario}"

    class Meta():
        verbose_name = "Mi Curso"
        verbose_name_plural = "Mis Cursos"
        ordering = ("dia", "horario", "nivel", )



class Profesores(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    email = models.EmailField( max_length=254)

    def __str__(self) -> str:

        return f"Nombre y apellido: {self.nombre} , {self.apellido} - Email: {self.email}"



class Alumnos(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    email = models.EmailField( max_length=254)

    def  __str__(self) -> str:

        return f"Nombre y apellido: {self.nombre} , {self.apellido} - Edad: {self.edad} - Email: {self.email}"


class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', blank=True, null=True)

    def __str__(self) -> str:
        return f"user: {self.user}  / imagen: {self.imagen}"

