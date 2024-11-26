from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Institucion
from .models import Carrera
from .models import Plan
from .models import Persona

class InstitucionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institucion
        fields = "__all__"

class CarreraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"

