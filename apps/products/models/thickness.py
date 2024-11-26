# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

from .measure import Measure

class Thickness(models.Model):
    measure_thickness = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name='thicknesses')
    number_thickness = models.CharField(max_length=255)

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Thickness')
        verbose_name_plural = _('Thicknesses')

    def __str__(self):
        return self.number_thickness + str(self.measure_thickness.abbreviation_measure)