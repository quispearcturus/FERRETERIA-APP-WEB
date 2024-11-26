from django.db import models
from gestion.models import Persona
from gestion.models import Plan
from unidades.models import UnidadDidactica

# Create your models here.

class Estudiante(models.Model):

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    foto = models.ImageField(blank=True)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.persona.nombre} {self.persona.apellido_paterno} {self.persona.apellido_materno}"
    
class PlanEstudiante(models.Model):

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.plan.nombre} {self.estudiante.persona.nombre}"

class Matricula(models.Model):

    plan_estudiante = models.ForeignKey(PlanEstudiante, on_delete=models.CASCADE)
    ciclo = models.IntegerField()

    def __str__(self):
        return f"{self.plan_estudiante.estudiante.persona.nombre} {self.plan_estudiante.estudiante.persona.apellido_paterno} {self.plan_estudiante.estudiante.persona.apellido_materno}"

class DetalleMatricula(models.Model):

    unidad_didactica = models.ForeignKey(UnidadDidactica, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    nota = models.IntegerField()
    estado_curso = models.BooleanField(blank=True)
    estado_modulo = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.unidad_didactica.nombre} {self.matricula.plan_estudiante.plan.nombre}"
