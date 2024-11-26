from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'institucion', views.InstitucionViewSet)
router.register(r'carrera', views.CarreraViewSet)
router.register(r'plane', views.PlanViewSet)
router.register(r'persona', views.PersonaViewSet)

urlpatterns = [
    path('', include(router.urls))
]


