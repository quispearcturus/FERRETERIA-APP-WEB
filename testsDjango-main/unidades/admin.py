from django.contrib import admin

from unidades.models import Modulo
from unidades.models import TipoUnidad
from unidades.models import UnidadDidactica
from unidades.models import TipoCompetencia
from unidades.models import Competencia
from unidades.models import Capacidad
from unidades.models import Indicador
from unidades.models import Contenido

# Register your models here.

admin.site.register(Modulo)
admin.site.register(TipoUnidad)
admin.site.register(UnidadDidactica)
admin.site.register(TipoCompetencia)
admin.site.register(Competencia)
admin.site.register(Capacidad)
admin.site.register(Indicador)
admin.site.register(Contenido)