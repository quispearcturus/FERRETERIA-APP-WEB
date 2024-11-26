from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import CertificadoModular
from .models import TipoEducacion
from .models import CertificadoEducacion
from .models import TipoAuxiliar
from .models import CertificadoAuxiliar

class CertificadoModularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertificadoModular
        fields = "__all__"

class TipoEducacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoEducacion
        fields = "__all__"

class CertificadoEducacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertificadoEducacion
        fields = "__all__"

class TipoAuxiliarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoAuxiliar
        fields = "__all__"

class CertificadoAuxiliarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertificadoAuxiliar
        fields = "__all__"