# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

from .measure import Measure

class Length(models.Model):
    measure_lenght = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name='lenghts')
    number_lenght = models.CharField(max_length=255)

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Length')
        verbose_name_plural = _('Lengths')
    
    def __str__(self):
        return self.number_lenght + str(self.measure_lenght.abbreviation_measure)