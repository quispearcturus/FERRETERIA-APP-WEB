# myapp/templatetags/custom_filters.py
from django import template
from decimal import Decimal



register = template.Library()

@register.filter
def multiply(value1, value2):
    try:
        return value1 * value2
    except (TypeError, ValueError):
        return 0

@register.filter
def grav(obj):
    t = sum(d.quantity * d.unit_price for d in obj)
    i = Decimal(t) * Decimal(0.18)
    return (t-i).quantize(Decimal('0.00'))

@register.filter
def igv(obj):
    t = sum(d.quantity * d.unit_price for d in obj)
    return (Decimal(t) * Decimal(0.18)).quantize(Decimal('0.00'))
    
@register.filter
def total(obj):
    t = sum(d.quantity * d.unit_price for d in obj)
    return t