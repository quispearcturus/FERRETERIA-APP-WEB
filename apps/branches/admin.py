# ZeroPaul
from django.contrib import admin
from apps.branches.models.branch import Branch
from apps.branches.models.stock import Stock, StockDetail
from apps.branches.models.store import Store


admin.site.register(Branch)
admin.site.register(Stock)
admin.site.register(StockDetail)
admin.site.register(Store)
