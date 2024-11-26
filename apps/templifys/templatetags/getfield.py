from django import template
from datetime import datetime

register = template.Library()

@register.filter
def getfield(obj, field_name):
    field = getattr(obj, field_name, None)
    if isinstance(field, datetime):
        field = field.date()
    return field
