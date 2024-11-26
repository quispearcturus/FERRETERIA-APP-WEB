from django.urls import path, include
from .models import Modulo
from .models import TipoUnidad
from .models import UnidadDidactica
from .models import TipoCompetencia
from .models import Competencia
from .models import Capacidad
from .models import Indicador
from .models import Contenido
from rest_framework import routers, serializers, viewsets

class ModuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modulo
        fields = "__all__"

class TipoUnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = "__all__"

class UnidadDidacticaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadDidactica
        fields = "__all__"

class TipoCompetenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCompetencia
        fields = "__all__"

class CompetenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competencia
        fields = "__all__"

class CapacidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Capacidad
        fields = "__all__"

class IndicadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicador
        fields = "__all__"

class ContenidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contenido
        fields = "__all__"