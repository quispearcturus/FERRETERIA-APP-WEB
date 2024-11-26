from django.contrib import admin

from gestion.models import Institucion
from gestion.models import Carrera
from gestion.models import Plan
from gestion.models import Persona

# Register your models here.

admin.site.register(Institucion)
admin.site.register(Carrera)
admin.site.register(Plan)
admin.site.register(Persona)