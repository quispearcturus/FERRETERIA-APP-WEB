# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

class Polygon(models.Model):
    name_polygon = models.CharField(max_length=255, default='I')

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Polygon')
        verbose_name_plural = _('Polygons')

    def __str__(self):
        if self.pk is not None:
            a = ' x '.join(str(side) for side in self.polygon_sides.all())
            if self.name_polygon == 'I':
                self.name_polygon = a
                self.save()
            return a
        else:
            return self.name_polygon
        
    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.name_polygon = ' x '.join(str(side) for side in self.polygon_sides.all())
        super(Polygon, self).save(*args, **kwargs)