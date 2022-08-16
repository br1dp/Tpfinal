from django.contrib import admin

from app_1.models import Profesores
from app_1.models import Alumnos
from app_1.models import Cursos

class CursosAdmin(admin.ModelAdmin):
    list_display = ['nivel', 'dia', 'horario', 'profesor']
    search_fields = ['nombre']


admin.site.register(Cursos, CursosAdmin)
admin.site.register(Alumnos)
admin.site.register(Profesores)

