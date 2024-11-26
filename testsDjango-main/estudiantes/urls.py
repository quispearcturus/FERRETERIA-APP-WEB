from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'estudiante', views.EstudianteViewSet)
router.register(r'plan-estudiante', views.PlanEstudianteViewSet)
router.register(r'matricula', views.MatriculaViewSet)
router.register(r'detalle-matricula', views.DetalleMatriculaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
