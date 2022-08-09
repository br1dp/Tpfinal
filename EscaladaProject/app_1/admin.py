from django.contrib import admin

from app_1.models import Profesores
from app_1.models import Alumnos
from app_1.models import Cursos

admin.site.register(Cursos)
admin.site.register(Alumnos)
admin.site.register(Profesores)
