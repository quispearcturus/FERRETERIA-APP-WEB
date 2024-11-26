from django.shortcuts import render
from rest_framework import viewsets
from .models import Modulo
from .models import TipoUnidad
from .models import UnidadDidactica
from .models import TipoCompetencia
from .models import Competencia
from .models import Capacidad
from .models import Indicador
from .models import Contenido
from .serializers import ModuloSerializer
from .serializers import TipoUnidadSerializer
from .serializers import UnidadDidacticaSerializer
from .serializers import TipoCompetenciaSerializer
from .serializers import CompetenciaSerializer
from .serializers import CapacidadSerializer
from .serializers import IndicadorSerializer
from .serializers import ContenidoSerializer
# Create your views here.

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class TipoUnidadViewSet(viewsets.ModelViewSet):
    queryset = TipoUnidad.objects.all()
    serializer_class = TipoUnidadSerializer

class UnidadDidacticaViewSet(viewsets.ModelViewSet):
    queryset = UnidadDidactica.objects.all()
    serializer_class = UnidadDidacticaSerializer

class TipoCompetenciaViewSet(viewsets.ModelViewSet):
    queryset = TipoCompetencia.objects.all()
    serializer_class = TipoCompetenciaSerializer

class CompetenciaViewSet(viewsets.ModelViewSet):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer

class CapacidadViewSet(viewsets.ModelViewSet):
    queryset = Capacidad.objects.all()
    serializer_class = CapacidadSerializer

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer