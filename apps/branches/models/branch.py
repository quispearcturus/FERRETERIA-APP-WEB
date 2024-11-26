# ZeroPaul
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

class Branch(models.Model):
    # fields
    branch_name = models.CharField(max_length=255)
    branch_address = models.CharField(max_length=255)
    branch_status = models.BooleanField(default=True)
    branch_principal = models.BooleanField(default=False)

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Branch')
        verbose_name_plural = _('Branches')

    def __str__(self):
        filial = None
        if self.branch_principal:
            filial = 'Principal Filial'
        else:
            filial = 'Sub Filial'
        return f'{ self.branch_name } - { filial }'
    
    def save(self, *args, **kwargs):
        if self.branch_principal:
            Branch.objects.filter(~Q(pk=self.pk), branch_principal=True).update(branch_principal=False)
        super(Branch, self).save(*args, **kwargs)