from django.db import models
from gestion.models import Plan

# Create your models here.
NUMERO_MODULO=[
    ('Modulo 1','Modulo 1'),
    ('Modulo 2','Modulo 2'),
    ('Modulo 3','Modulo 3'),
]

NUMERO_COMPETENCIA=[
    ('UC1','UC1'),
    ('UC2','UC2'),
    ('UC3','UC3'),
    ('UC4','UC4'),
    ('CE1','CE1'),
    ('CE2','CE2'),
    ('CE3','CE3'),
    ('CE4','CE4'),
]

NUMERO_CAPACIDAD=[
    ('C1','C1'),
    ('C2','C2'),
    ('C3','C3'),
    ('C4','C4'),
    ('C5','C5'),
    ('C6','C6'),
    ('C7','C7'),
    ('C8','C8'),
    ('C9','C9'),
]

NUMERO_INDICADOR=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
]

class Modulo(models.Model):

    numero = models.CharField(max_length=50, choices=NUMERO_MODULO)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.numero} {self.nombre}"

class TipoUnidad(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class UnidadDidactica(models.Model):

    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoUnidad, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    horas = models.IntegerField()
    ciclo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
class TipoCompetencia(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Competencia(models.Model):

    tipo = models.ForeignKey(TipoCompetencia, on_delete=models.CASCADE)
    unidad_didactica = models.ForeignKey(UnidadDidactica, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50, choices=NUMERO_COMPETENCIA)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.numero} {self.descripcion}"
    
class Capacidad(models.Model):

    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50, choices=NUMERO_CAPACIDAD)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.numero} {self.descripcion}"

class Indicador(models.Model):

    capacidad = models.ForeignKey(Capacidad, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50, choices=NUMERO_INDICADOR)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.numero} {self.descripcion}"

class Contenido(models.Model):

    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.descripcion}"
