# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Noticia, Categoria
from django.conf import settings
from django import forms
from configuracoes.models import Modulo

""" Admin Noticia """
class AdminNoticia(admin.ModelAdmin):
    list_display = ('vch_titulo', 'dat_noticia', 'boo_ativo' )# defini os campos que vao aparecer no formulario
    exclude = ('dat_noticia',)# esconde o campo dat_noticia do formulario
    date_hierarchy = 'dat_noticia'
    """ Chama os javascript para o editor html """
    class Media:
        model = Noticia
        js = (settings.MEDIA_URL + "/js/editorHtml/jscripts/tiny_mce/tiny_mce.js",# insere o javascript do editor html na pagina
              settings.MEDIA_URL + "/js/editorHtml/textarea.js",)# insere o javascript do editor html na pagina


if Modulo.objects.filter(modulo = 'noticia'): 
    admin.site.register(Noticia, AdminNoticia)
    admin.site.register(Categoria)
    