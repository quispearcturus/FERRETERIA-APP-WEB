# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

class Measure(models.Model):
    name_measure = models.CharField(max_length=255)
    abbreviation_measure = models.CharField(max_length=255)
    
    class Meta:
        # ordering = ['field',]
        verbose_name = _('Measure')
        verbose_name_plural = _('Measures')

    def __str__(self):
        return self.name_measure