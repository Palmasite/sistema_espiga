from django.contrib import admin
from models import Departamento, Contato

from configuracoes.models import Modulo

if Modulo.objects.filter(modulo = 'contato'):
    admin.site.register(Departamento)
    admin.site.register(Contato)



