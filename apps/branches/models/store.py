# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.branches.models.branch import Branch

class Store(models.Model):
    # fields
    store_name = models.CharField(max_length=255)
    store_address = models.CharField(max_length=255)
    store_status = models.BooleanField(default=True)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='store_branch'
    )
    
    class Meta:
        # ordering = ['field',]
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')

    def __str__(self):
        return f'{self.branch.branch_name}-{self.store_name}'