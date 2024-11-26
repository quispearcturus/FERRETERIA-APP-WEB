from django.contrib import admin

from estudiantes.models import Estudiante
from estudiantes.models import PlanEstudiante
from estudiantes.models import Matricula
from estudiantes.models import DetalleMatricula

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(PlanEstudiante)
admin.site.register(Matricula)
admin.site.register(DetalleMatricula)