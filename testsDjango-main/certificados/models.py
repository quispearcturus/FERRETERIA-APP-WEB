from django.db import models

from estudiantes.models import DetalleMatricula

# Create your models here.
class CertificadoModular(models.Model):

    detalle_matricula = models.ForeignKey(DetalleMatricula, on_delete=models.CASCADE)
    registro_inst = models.CharField(max_length=15, blank=True)
    fecha = models.DateField()
    firma = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.detalle_matricula.matricula.plan_estudiante.estudiante.persona.nombre} {self.registro_inst}"

class TipoEducacion(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class CertificadoEducacion(models.Model):

    detalle_matricula = models.ForeignKey(DetalleMatricula, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoEducacion, on_delete=models.CASCADE)
    registro_inst = models.CharField(max_length=15, blank=True)
    registro_minedu = models.CharField(max_length=15, blank=True)
    fecha = models.DateField()
    firma = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.detalle_matricula.matricula.plan_estudiante.estudiante.persona.nombre} {self.registro_inst}"
    
class TipoAuxiliar(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class CertificadoAuxiliar(models.Model):

    detalle_matricula = models.ForeignKey(DetalleMatricula, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoAuxiliar, on_delete=models.CASCADE)
    registro_inst = models.CharField(max_length=15, blank=True)
    fecha = models.DateField()
    firma = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.detalle_matricula.matricula.plan_estudiante.estudiante.persona.nombre} {self.registro_inst}"
