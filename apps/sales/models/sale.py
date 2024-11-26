# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.products.models.product import Product
from apps.sales.models.voucher import NumerationVoucher


class Sale(models.Model):
    # fields
    customer = models.CharField(max_length=255)
    numeration_voucher = models.ForeignKey(
        NumerationVoucher, on_delete=models.CASCADE,
        related_name='sales_numeration_voucher'
    )
    date_sale = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Sale')
        verbose_name_plural = _('Sales')

    def __str__(self):
        return f'{ self.customer} - { self.date_sale.date()}'
    
    def save(self, *args, **kwargs):
        # self.numeration_voucher.gen_correlative()
        print(self.id)
        super(Sale, self).save(*args, **kwargs)
        
    @property
    def total(self):
        return sum(detail.subtotal for detail in self.sale_sale_detail.all())
    
    def get_serie_number(self):
        return self.numeration_voucher.serie_voucher, self.numeration_voucher.number


class SaleDetail(models.Model):
    # fields
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE,
        related_name='sale_sale_detail'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_sale_detail'
    )
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # ordering = ['name',]
        verbose_name = _('Sale Detail')
        verbose_name_plural = _('Sale Details')

    def __str__(self):
        return f'{self.product.__str__()} - {self.quantity}'
    
    @property
    def subtotal(self):
        return self.quantity * self.unit_price
