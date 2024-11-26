from django.shortcuts import render
from rest_framework import viewsets
from .models import Estudiante
from .models import PlanEstudiante
from .models import Matricula
from .models import DetalleMatricula
from .serializers import EstudianteSerializer
from .serializers import PlanEstudianteSerializer
from .serializers import MatriculaSerializer
from .serializers import DetalleMatriculaSerializer
# Create your views here.

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class PlanEstudianteViewSet(viewsets.ModelViewSet):
    queryset = PlanEstudiante.objects.all()
    serializer_class = PlanEstudianteSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class DetalleMatriculaViewSet(viewsets.ModelViewSet):
    queryset = DetalleMatricula.objects.all()
    serializer_class = DetalleMatriculaSerializer


