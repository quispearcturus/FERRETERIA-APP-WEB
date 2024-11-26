from django.urls import path, include
from .models import Estudiante
from .models import PlanEstudiante
from .models import Matricula
from .models import DetalleMatricula
from rest_framework import routers, serializers, viewsets

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"

class PlanEstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanEstudiante
        fields = "__all__"

class MatriculaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"

class DetalleMatriculaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleMatricula
        fields = "__all__"