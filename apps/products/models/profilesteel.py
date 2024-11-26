# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .shape import Shape
from .texture import Texture
from .polygon import Polygon
from .thickness import Thickness
from .length import Length
from .steel import Steel
from .product import Product


class TypeProfileSteel(models.Model):
    # fields
    name_profile_steel = models.CharField(max_length=255)

    class Meta:
        # ordering = ['name_profile_steel',]
        verbose_name = _('TypeProfileSteel')
        verbose_name_plural = _('TypeProfileSteels')

    def __str__(self):
        return self.name_profile_steel


class ProfileSteel(models.Model):

    type_profile_steel = models.ForeignKey(
        TypeProfileSteel, on_delete=models.CASCADE,
        related_name='profile_steels_tps'
    )
    shape = models.ForeignKey(
        Shape, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='shapes_tps'
    )
    texture = models.ForeignKey(
        Texture, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='textures_tps'
    )
    shape = models.ForeignKey(
        Shape, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='shapes_tps'
    )
    polygon = models.ForeignKey(
        Polygon, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='polygons_tps'
    )

    thickness = models.ForeignKey(
        Thickness, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='thickness_tps'
    )
    length = models.ForeignKey(
        Length, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='lengths_tps'
    )
    steel = models.ForeignKey(
        Steel, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='steels_tps'
    )

    name_origin = models.CharField(
        max_length=300, default='Nullmx', unique=True)
    
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='profile_steels_product')

    class Meta:
        # ordering = ['field',]
        verbose_name = _('ProfileSteel')
        verbose_name_plural = _('ProfileSteels')

    def get_name_complete(self):
        name_complete = None
        name_complete = f"{ self.type_profile_steel.name_profile_steel } " if self.type_profile_steel is not None else ''
        name_complete += f"{ self.shape.name_shape } " if self.shape is not None else ''
        name_complete += f"{ self.texture.name_texture } " if self.texture is not None else ''
        name_complete += f"{ self.polygon.__str__() } " if self.polygon is not None else ''
        name_complete += f" x { self.thickness.__str__() } " if self.thickness is not None else ''
        name_complete += f" x { self.length.__str__() } " if self.length is not None else ''
        name_complete += f"{ self.steel.abbreviation_steel } " if self.steel is not None else ''
        return name_complete.strip()

    def __str__(self):
        return self.get_name_complete()

    def clean(self):
        super().clean()
        self.name_origin = self.get_name_complete()
        product = ProfileSteel.objects.filter(name_origin=self.name_origin)
        if product.exists():
            if self.pk != product.first().id:
                raise ValidationError(f"'{self.name_origin}' already exists.")

    def save(self, *args, **kwargs):
        self.name_origin = self.get_name_complete()
        self.clean()

        super(ProfileSteel, self).save(*args, **kwargs)