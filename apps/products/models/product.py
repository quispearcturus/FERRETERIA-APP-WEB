# ZeroPaul
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    class Meta:
        # ordering = ['field',]
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    # def __str__(self):
    #     return self.get_reverse_relation_name()
    
    def __str__(self):
        if not hasattr(self, '_full_name_cache'):
            self._full_name_cache = self.get_reverse_relation_name()
        return self._full_name_cache
    
    def get_reverse_relation_name(self):
        # print("get reversed")
        r = None
        related_names_all = self.get_related_names()
        for related_name in related_names_all:
            if hasattr(self, related_name):
                related_instance = getattr(self, related_name)
                try:
                    if related_instance.exists():
                        r = related_instance.__str__()
                except Exception as e:
                    # print('error', e)
                    r = related_instance.__str__()
                break
            
            else:
                r = f'{self.id} product is not assigned to any type'
        return r
            

    def get_related_names(self):
        product_meta = Product._meta
        related_names = []

        for field in product_meta.get_fields():
            if field.is_relation and field.related_name:
                # if not field.related_name.startswith(('pric', 'pra')):
                related_names.append(field.related_name)
        
        related_names.append('null')

        return related_names

# Proxy Model


class ProductsProfileSteel(Product):
    class Meta:
        proxy = True


class ProductsWelding(Product):
    class Meta:
        proxy = True
