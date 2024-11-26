# forms.py
# from django import forms
from apps.templifys.models import ModelChoiceField
from apps.templifys.models import ModelForm
from apps.templifys import widgets

from apps.products.models.product import Product
from apps.products.models.profilesteel import ProfileSteel, TypeProfileSteel
from apps.products.models.welding import Welding


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

from django.db import models
class DynamicWidget():
    fields_widgets = {
        models.CharField: widgets.TextInput,
        models.IntegerField: widgets.NumberInput,
        models.EmailField: widgets.EmailInput,
        models.DateField: widgets.DateInput(attrs={'type': 'date'}),
        models.BooleanField: widgets.CheckboxInput,
        models.TextField: widgets.Textarea,
        models.FloatField: widgets.NumberInput,
        models.DecimalField: widgets.NumberInput,
        models.FileField: widgets.ClearableFileInput,
        models.ImageField: widgets.ClearableFileInput,
        models.URLField: widgets.URLInput,
        models.PositiveIntegerField: widgets.NumberInput,
        models.PositiveSmallIntegerField: widgets.NumberInput,
        models.SlugField: widgets.TextInput,
        models.TimeField: widgets.TimeInput(attrs={'type': 'time'}),
        models.GenericIPAddressField: widgets.TextInput,
        models.ForeignKey: widgets.Select(),
        models.ManyToManyField: widgets.CheckboxSelectMultiple,
        models.OneToOneField: widgets.Select(),
    }

    def __init__(self, model, fields):
        self.model = model
        self.fields = fields

    def generate_widgets(self):
        widgets = {}
        for field in self.model._meta.get_fields():
            if field.name in self.fields:
                widget = self.fields_widgets.get(type(field))
                widgets[field.name] = widget
                # print(f'Nombre: {field.name}, Tipo: {widget}')
        return widgets


class ProfileSteelForm(ModelForm):
    class Meta():
        model = ProfileSteel
        fields = ['type_profile_steel', 'texture', 'shape',
                  'polygon', 'thickness', 'length', 'steel']
        widgets = DynamicWidget(model=model, fields=fields).generate_widgets()
   


class WeldingForm(ModelForm):
    class Meta:
        model = Welding
        fields = ['brand', 'type_welding', 'thickness', 'package']
        widgets = DynamicWidget(model=model, fields=fields).generate_widgets()


# from django.forms import ModelForm, Textarea
# from apps.templifys.widgets import Select

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         widgets = {
#             'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }
