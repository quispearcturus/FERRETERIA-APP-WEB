# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

from .measure import Measure
from .polygon import Polygon


class Side(models.Model):
    name_side = models.CharField(max_length=255)
    measure_side = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name='sides')

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Side')
        verbose_name_plural = _('Sides')

    def __str__(self):
        return self.name_side + ' ' + str(self.measure_side.abbreviation_measure)


class GroupSide(models.Model):
    # fields
    side = models.ForeignKey(Side, on_delete=models.CASCADE, related_name='group_sides')
    polygon = models.ForeignKey(Polygon, on_delete=models.CASCADE, related_name='polygon_sides')

    class Meta:
        # ordering = ['name',]
        verbose_name = _('GroupSide')
        verbose_name_plural = _('GroupSides')

    def __str__(self):
        return str(self.side.name_side)
