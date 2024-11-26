# ZeroPaul
from django.contrib import admin
from apps.sales.models.sale import Sale, SaleDetail
from apps.sales.models.voucher import TypeVoucher, SerieVoucher, NumerationVoucher

class SaleDetailInline(admin.StackedInline):
    model = SaleDetail
    extra = 0
    
    readonly_fields = ('subtotal',)

    def subtotal(self, obj):
        if obj and obj.quantity is not None:
            sub = obj.subtotal
        else:
            sub = '-'
        return str(sub)
    subtotal.short_description = 'sub total'
    
    
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    inlines = [SaleDetailInline]
    readonly_fields = ('total',)
    save_on_top = True
    
    class Media:
        js = ('js/asave.js',)
    
    def total(self, obj):
        return obj.total
    total.short_description = 'total'


# admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.register(TypeVoucher)
admin.site.register(SerieVoucher)
admin.site.register(NumerationVoucher)
