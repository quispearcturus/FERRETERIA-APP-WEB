# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeVoucher(models.Model):
    # fields
    voucher_name = models.CharField(max_length=255, unique=True)
    voucher_status = models.BooleanField(default=True)

    class Meta:
        # ordering = ['voucher_name',]
        verbose_name = _('TypeVoucher')
        verbose_name_plural = _('TypeVoucher s')

    def __str__(self):
        return f'{self.voucher_name}'

class SerieVoucher(models.Model):
    # fields
    type_voucher = models.ForeignKey(
        TypeVoucher, on_delete=models.CASCADE,
        related_name='serie_vouchers_type_voucher'
    )
    serial_number = models.CharField(max_length=4, unique=True)
    serial_status = models.BooleanField(default=True)

    class Meta:
        # ordering = ['serial_number',]
        verbose_name = _('SerieVoucher')
        verbose_name_plural = _('SerieVouchers')

    def __str__(self):
        return f'{self.type_voucher.voucher_name}-{self.serial_number}'
    
class NumerationVoucher(models.Model):
    # fields
    serie_voucher = models.ForeignKey(
        SerieVoucher, on_delete=models.CASCADE,
        related_name='numeration_vouchers_serie_voucher'
    )
    number = models.IntegerField()

    class Meta:
        # ordering = ['name',]
        verbose_name = _('NumerationVoucher')
        verbose_name_plural = _('NumerationVouchers')

    def __str__(self):
        return f'{self.serie_voucher.__str__()}-{self.number}'
    
    def gen_correlative(self):
        last_number = NumerationVoucher.objects.all().filter(serie_voucher=self.serie_voucher).order_by('-number').first()
        print("---", last_number)
        gen_number = last_number + 1 if last_number else 1
        self.number = gen_number
        # self.save()