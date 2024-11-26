from django.contrib import admin

from certificados.models import CertificadoModular
from certificados.models import TipoEducacion
from certificados.models import CertificadoEducacion
from certificados.models import TipoAuxiliar
from certificados.models import CertificadoAuxiliar

# Register your models here.

admin.site.register(CertificadoModular)
admin.site.register(TipoEducacion)
admin.site.register(CertificadoEducacion)
admin.site.register(TipoAuxiliar)
admin.site.register(CertificadoAuxiliar)