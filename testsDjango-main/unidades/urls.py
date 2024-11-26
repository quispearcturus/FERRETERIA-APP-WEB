from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'modulo', views.ModuloViewSet)
router.register(r'tipo-unidad', views.TipoUnidadViewSet)
router.register(r'unidad-didactica', views.UnidadDidacticaViewSet)
router.register(r'tipo-competencia', views.TipoCompetenciaViewSet)
router.register(r'competencia', views.CompetenciaViewSet)
router.register(r'capacidad', views.CapacidadViewSet)
router.register(r'indicador', views.IndicadorViewSet)
router.register(r'contenido', views.ContenidoViewSet)

urlpatterns = [
    path('', include(router.urls))
]