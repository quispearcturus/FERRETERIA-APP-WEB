# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _
from .product import Product
from apps.products.models.thickness import Thickness


class Brand(models.Model):
    # fields
    brand_name = models.CharField(max_length=255)

    class Meta:
        # ordering = ['name',]
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return f'{self.brand_name}'

class TypeWelding(models.Model):
    # fields
    tw_name = models.CharField(max_length=255)

    class Meta:
        # ordering = ['tw_name',]
        verbose_name = _('TypeWelding')
        verbose_name_plural = _('TypeWeldings')

    def __str__(self):
        return f'{self.tw_name}'

class Package(models.Model):
    # fields
    pkg_name = models.CharField(max_length=255)

    class Meta:
        # ordering = ['pkg_name',]
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')

    def __str__(self):
        return f'{self.pkg_name}'


class Welding(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE,
        related_name='welds_brand'
    )
    type_welding = models.ForeignKey(
        TypeWelding, on_delete=models.CASCADE,
        related_name='welds_tw'
    )
    thickness = models.ForeignKey(
        Thickness, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='welds_thickness'
    )
    # amper
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE,
        related_name='welds_package'
    )
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE,
        related_name='welds_product'
    )

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Welding')
        verbose_name_plural = _('Weldings')

    def __str__(self):
        return f'{self.brand.brand_name} - {self.type_welding.tw_name} - {self.package.pkg_name}'
