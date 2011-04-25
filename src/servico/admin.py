# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from admin_utils import MeuTabularInline, MeuModelAdmin

from servico.models import Servico, LinkServico
from configuracoes.models import Modulo


class LinkServicoInline(MeuTabularInline):
    extra = 1
    model = LinkServico

class ServicoAdmin(MeuModelAdmin):
    inlines = [LinkServicoInline, ] 
    class Media:
        model = Servico
        js = (settings.MEDIA_URL + "/js/editorHtml/jscripts/tiny_mce/tiny_mce.js", # insere o javascript do editor html na pagina
              settings.MEDIA_URL + "/js/editorHtml/textarea.js",)# insere o javascript do editor html na pagina

    
if Modulo.objects.filter(modulo='servico'): 
    admin.site.register(Servico, ServicoAdmin)

 

