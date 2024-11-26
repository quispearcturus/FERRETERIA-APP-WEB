import random
import string
from django.template.loader import render_to_string
from django.forms.utils import pretty_name

class WidgetGeneric:
    template_name = None
    obj_data = {}

    def gen_id(self, name):
        id = ('mx-'+name+'-')+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        return id

    def get_context(self):
        return {
            "widget": {
                'id': self.gen_id('datar')
            },
        }
        
    def render(self):
        context = self.get_context()
        return render_to_string(self.template_name, context)
    
    def __call__(self):
        return self.render()
        


class WidgetTable(WidgetGeneric):
    template_name = 'templifys/list/table.html'
    
    def __init__(self, context):
        self.context = context
    
    def get_context(self):
        context = super().get_context()
        context['obj_table'] = self.get_context
        context['heads'] = self.build_table()
        context['object_list'] = self.context['object_list']
        context['fields'] = self.get_fields(False)
        return context
    
    def get_fields(self, pretty=True):
        model = self.context['object_list'].model
        fields = [ pretty_name(field.name) if pretty else field.name for field in model._meta.get_fields() if not(field.is_relation) and field.name != 'id']
        return fields
        
    def build_table(self):
        model = self.context['object_list'].model
        heads = self.get_fields(True)
        
        return heads
        
        
        