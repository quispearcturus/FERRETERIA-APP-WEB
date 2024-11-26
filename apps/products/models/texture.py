# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _


class Texture(models.Model):
    name_texture = models.CharField(max_length=255)

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Texture')
        verbose_name_plural = _('Textures')

    def __str__(self):
        return self.name_texture
