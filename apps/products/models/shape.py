# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

class Shape(models.Model):
    name_shape = models.CharField(max_length=255)
    class Meta:
        # ordering = ['field',]
        verbose_name = _('Shape')
        verbose_name_plural = _('Shapes')

    def __str__(self):
        return self.name_shape