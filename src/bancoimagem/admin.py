# -*- coding: utf-8 -*-
from django.contrib import admin
from models import BancoImagem, Galeria
from django.conf import settings
from datetime import datetime
from admin_utils import MeuModelAdmin, MeuTabularInline 

try:
    import Image
except ImportError:
    from PIL import Image


""" Admin Banco de Imagem """
class AdminBancoImagemInline(MeuTabularInline):
    list_display = ('vch_titulo', 'dat_foto', 'vch_fotografo', 'foto')# define os campos que vao aparecer na consulta
    exclude = ('dat_foto', 'img_miniatura',)# esconde o campo dat_foto do formulario
    model = BancoImagem
        
        
class GaleriaAdmin(MeuModelAdmin):
    model = Galeria
    inlines = [AdminBancoImagemInline, ]
    
class BancoImagemAdmin(admin.ModelAdmin):
    list_display = ('vch_titulo', 'galeria')
    list_filter = ['galeria']
    model = BancoImagem
    
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(BancoImagem, BancoImagemAdmin)
 

