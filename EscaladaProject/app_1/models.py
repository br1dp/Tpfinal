from random import choices
from django.db import models

class Cursos(models.Model):

    nivel = models.CharField( max_length=50)

    dias = [
        ('Lunes','Lunes'), 
        ('Martes','Martes'),
        ('Miércoles','Miércoles'), 
        ('Jueves','Jueves'), 
        ('Viernes','Viernes'),
    ]
    dia = models.CharField(max_length=20, choices=dias, default='Lunes')

    horario = models.IntegerField()

    profesor = models.CharField( max_length=50)

    def __str__(self) -> str:
        return f"Niveles: {self.nivel}  / DIA: {self.dia}  Horarios: {self.horario}"

    class Meta():
        verbose_name = "Mi Curso"
        verbose_name_plural = "Mis Cursos"
        ordering = ("dia", "horario", "nivel", )

class Profesores(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    email = models.EmailField( max_length=254)

    def __str__(self) -> str:

        return f"Nombre y apellido: {self.nombre} , {self.apellido} -Cursos: {self.cursos} - Email: {self.email}"



class Alumnos(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    email = models.EmailField( max_length=254)

    def  __str__(self) -> str:

        return f"Nombre y apellido: {self.nombre} , {self.apellido} - Edad: {self.edad} - Email: {self.email}"

        

