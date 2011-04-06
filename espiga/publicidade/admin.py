# -*- ecoding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from publicidade.models import Publicidade
from configuracoes.models import Modulo


if Modulo.objects.filter(modulo = 'publicidade'): 
    admin.site.register(Publicidade)
    
    
    