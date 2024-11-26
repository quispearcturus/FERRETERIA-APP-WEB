from django.shortcuts import render
from rest_framework import viewsets
from .models import Institucion
from .models import Carrera
from .models import Plan
from .models import Persona
from .serializers import InstitucionSerializer
from .serializers import CarreraSerializer
from .serializers import PlanSerializer
from .serializers import PersonaSerializer

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

