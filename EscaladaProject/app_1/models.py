from django.db import models

class Cursos(models.Model):

    nivel = models.CharField( max_length=50)

    horario = models.IntegerField()

    profesor = models.CharField( max_length=50)

    def __str__(self) -> str:
        return f"Niveles: {self.nivel} - Horarios: {self.horario} - Profesor: {self.profesor}"

    class Meta():
        verbose_name = "Mi Curso"
        verbose_name_plural = "Mis Cursos"
        ordering = ("nivel",)


class Alumnos(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    email = models.EmailField( max_length=254)

    def  __str__(self) -> str:

        return f"Nombre y apellido: {self.nombre} , {self.apellido} - Edad: {self.edad} - Email: {self.email}"

        
class Profesores(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    nivel = models.CharField(max_length=50)

    email = models.EmailField( max_length=254)

    def __str__(self) -> str:

        return f"Nombre y apellido: {self.nombre} , {self.apellido} - Nivel: {self.nivel} - Email: {self.email}"

