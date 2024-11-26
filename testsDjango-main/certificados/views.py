from django.shortcuts import render
from rest_framework import viewsets
from .models import CertificadoModular
from .models import TipoEducacion
from .models import CertificadoEducacion
from .models import TipoAuxiliar
from .models import CertificadoAuxiliar
from .serializers import CertificadoModularSerializer
from .serializers import TipoEducacionSerializer
from .serializers import CertificadoEducacionSerializer
from .serializers import TipoAuxiliarSerializer
from .serializers import CertificadoAuxiliarSerializer
# Create your views here.

class CertificadoModularViewSet(viewsets.ModelViewSet):
    queryset = CertificadoModular.objects.all()
    serializer_class = CertificadoModularSerializer

class TipoEducacionViewSet(viewsets.ModelViewSet):
    queryset = TipoEducacion.objects.all()
    serializer_class = TipoEducacionSerializer

class CertificadoEducacionViewSet(viewsets.ModelViewSet):
    queryset = CertificadoEducacion.objects.all()
    serializer_class = CertificadoEducacionSerializer

class TipoAuxiliarViewSet(viewsets.ModelViewSet):
    queryset = TipoAuxiliar.objects.all()
    serializer_class = TipoAuxiliarSerializer

class CertificadoAuxiliarViewSet(viewsets.ModelViewSet):
    queryset = CertificadoAuxiliar.objects.all()
    serializer_class = CertificadoAuxiliarSerializer