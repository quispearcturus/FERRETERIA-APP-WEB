# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.branches.models.store import Store
from apps.products.models.product import Product

class Stock(models.Model):
    # fields
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE,
        related_name='stocks_store'
    )
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE,
        related_name='stocks_product'
    )
    min_stock = models.PositiveSmallIntegerField(default=15)
    total_quantity = models.IntegerField(default=0)

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')

    def __str__(self):
        return f'{self.store}-{self.product.__str__()}-{self.total_quantity}'
        
class StockDetail(models.Model):
    # fields
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='stockdetails_stock')
    # provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='stockdetails_provider')
    quantity = models.IntegerField()
    date_stock = models.DateTimeField(auto_now_add=True)
    add_stock = models.BooleanField(default=True)
    dump = models.BooleanField(default=False)

    class Meta:
        # ordering = ['name',]
        verbose_name = _('StockDetail')
        verbose_name_plural = _('StockDetails')

    def __str__(self):
        return f'{ self.stock } - { self.quantity } - { self.date_stock.date() }'