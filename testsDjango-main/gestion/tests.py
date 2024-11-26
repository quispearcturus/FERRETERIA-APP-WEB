from django.test import TestCase
from .models import Institucion, Carrera, Plan, Persona
from django.core.exceptions import ValidationError
from rest_framework.test import APIClient
from rest_framework import status

class InstitucionTestCase(TestCase):
    def test_institucion_nombre_vacio(self):
        with self.assertRaises(ValidationError):
            institucion = Institucion(nombre='', lugar='Ciudad de Prueba')
            institucion.full_clean()

    def test_institucion_lugar_vacio(self):
        with self.assertRaises(ValidationError):
            institucion = Institucion(nombre='Institución de Prueba', lugar='')
            institucion.full_clean()

    def test_institucion_str(self):
        institucion = Institucion.objects.create(
            nombre="Institución de Prueba",
            lugar="Ciudad de Prueba"
        )
        self.assertEqual(str(institucion), "Institución de Prueba")

class CarreraTestCase(TestCase):
    def test_carrera_nombre_vacio(self):
        institucion = Institucion.objects.create(
            nombre="Institución de Prueba",
            lugar="Ciudad de Prueba"
        )
        with self.assertRaises(ValidationError):
            carrera = Carrera(institucion=institucion, nombre='')
            carrera.full_clean()

    def test_carrera_str(self):
        institucion = Institucion.objects.create(
            nombre="Institución de Prueba",
            lugar="Ciudad de Prueba"
        )
        carrera = Carrera.objects.create(
            institucion=institucion,
            nombre="Carrera de Prueba"
        )
        self.assertEqual(str(carrera), "Carrera de Prueba")

class PlanTestCase(TestCase):
    def test_plan_nombre_vacio(self):
        institucion = Institucion.objects.create(
            nombre="Institución de Prueba",
            lugar="Ciudad de Prueba"
        )
        carrera = Carrera.objects.create(
            institucion=institucion,
            nombre="Carrera de Prueba"
        )
        with self.assertRaises(ValidationError):
            plan = Plan(carrera=carrera, nombre='')
            plan.full_clean()

    def test_plan_str(self):
        institucion = Institucion.objects.create(
            nombre="Institución de Prueba",
            lugar="Ciudad de Prueba"
        )
        carrera = Carrera.objects.create(
            institucion=institucion,
            nombre="Carrera de Prueba"
        )
        plan = Plan.objects.create(
            carrera=carrera,
            nombre="Plan de Prueba"
        )
        self.assertEqual(str(plan), "Plan de Prueba")

class PersonaTestCase(TestCase):
    def test_persona_nombre_vacio(self):
        with self.assertRaises(ValidationError):
            persona = Persona(nombre='', apellido_paterno="Doe", apellido_materno="Smith")
            persona.full_clean()

    def test_persona_apellido_paterno_vacio(self):
        with self.assertRaises(ValidationError):
            persona = Persona(nombre="John", apellido_paterno="", apellido_materno="Smith")
            persona.full_clean()

    def test_persona_apellido_materno_vacio(self):
        with self.assertRaises(ValidationError):
            persona = Persona(nombre="John", apellido_paterno="Doe", apellido_materno="")
            persona.full_clean()

    def test_persona_str(self):
        persona = Persona.objects.create(
            nombre="John",
            apellido_paterno="Doe",
            apellido_materno="Smith"
        )
        self.assertEqual(str(persona), "John Doe Smith")
