# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

class Steel(models.Model):
    name_steel = models.CharField(max_length=255)
    abbreviation_steel = models.CharField(max_length=255)
    
    class Meta:
        # ordering = ['field',]
        verbose_name = _('Steel')
        verbose_name_plural = _('Steels')

    def __str__(self):
        return self.abbreviation_steel