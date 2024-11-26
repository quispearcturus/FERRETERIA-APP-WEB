# ZeroPaul
from django.contrib import admin
from apps.products.models.measure import Measure
from apps.products.models.thickness import Thickness
from apps.products.models.length import Length
from apps.products.models.side import Side, GroupSide
from apps.products.models.polygon import Polygon
from apps.products.models.texture import Texture
from apps.products.models.shape import Shape
from apps.products.models.steel import Steel
from apps.products.models.profilesteel import TypeProfileSteel, ProfileSteel
from apps.products.models.product import Product, ProductsProfileSteel, ProductsWelding
from apps.products.models.welding import Welding, Brand, Package, TypeWelding

class GroupSideInline(admin.TabularInline):
    model = GroupSide
    extra = 1

@admin.register(Polygon)
class PoligonoAdmin(admin.ModelAdmin):
    inlines = [GroupSideInline]
    readonly_fields = ('name_polygon',)
    
@admin.register(ProfileSteel)
class ProfileSteelAdmin(admin.ModelAdmin):
    readonly_fields = ('name_origin',)


class ProfileSteelInline(admin.StackedInline):
    model = ProfileSteel
    exclude = ['name_origin',]
    extra = 1


class WeldingInline(admin.StackedInline):
    model = Welding
    # exclude = ['field',]
    extra = 1

@admin.register(ProductsProfileSteel)
class ProductProfileSteelAdmin(admin.ModelAdmin):
    inlines = [ProfileSteelInline]

    def get_queryset(self, request):
        return super().get_queryset(request).filter(profile_steels_product__isnull=False)

@admin.register(ProductsWelding)
class ProductWeldingAdmin(admin.ModelAdmin):
    inlines = [WeldingInline]

    def get_queryset(self, request):
        return super().get_queryset(request).filter(welds_product__isnull=False)

    
admin.site.register(Measure)
admin.site.register(Thickness)
admin.site.register(Length)
admin.site.register(Side)
admin.site.register(GroupSide)
admin.site.register(Texture)
admin.site.register(Shape)
admin.site.register(Steel)
admin.site.register(TypeProfileSteel)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Package)
admin.site.register(TypeWelding)
admin.site.register(Welding)