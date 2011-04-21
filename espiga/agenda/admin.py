# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Agenda, Eventos
from configuracoes.models import Modulo
from django.conf import settings

class AdminAgenda(admin.ModelAdmin):
    model = Agenda
    
class AdminEventos(admin.ModelAdmin):
    class Media:
        model = Eventos
        js = (settings.MEDIA_URL + "/js/editorHtml/jscripts/tiny_mce/tiny_mce.js",# insere o javascript do editor html na pagina
              settings.MEDIA_URL + "/js/editorHtml/textarea.js",)# insere o javascript do editor html na pagina

    
if Modulo.objects.filter(modulo = 'agenda'):
    admin.site.register(Agenda, AdminAgenda)
    admin.site.register(Eventos, AdminEventos)