from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'certificado-modular', views.CertificadoModularViewSet)
router.register(r'tipo-educacion', views.TipoEducacionViewSet)
router.register(r'certificado-educacion', views.CertificadoEducacionViewSet)
router.register(r'tipo-auxiliar', views.TipoAuxiliarViewSet)
router.register(r'certificado-auxiliar', views.CertificadoAuxiliarViewSet)

urlpatterns = [
    path('', include(router.urls))
]
