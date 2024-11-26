import random
import string
from django.template.loader import render_to_string

class WidgetTemplify:
    template_name = None
    obj_data = {}

    def gen_id(self, name):
        id = ('mx-'+name+'-')+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        return id

    def set_context(self, contxt):
        self.obj_data = contxt
        
    def render(self):
        self.obj_data['id'] = self.gen_id('datar')
        context = {
            "widget": self.obj_data
        }
        return render_to_string(self.template_name, context)
        


class Scoreboard(WidgetTemplify):
    template_name = 'templifys/dashboard/scoreboard.html'
    
    def __init__(self, parser):
        self.set_context(parser)