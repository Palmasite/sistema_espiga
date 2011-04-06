# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from enquete.models import Enquete, Escolha
from admin_utils import MeuModelAdmin, MeuTabularInline
#from autenticacao.models import UserRH
from django.conf import settings
from configuracoes.models import Modulo


""" Tabular inline de escolha """
class EscolhaInline(MeuTabularInline):
    fieldsets = ((None,{'fields':('escolha',)}),)
    model = Escolha  
    #max_num = 3

""" Admin Enquete """
class EnqueteAdmin(MeuModelAdmin):        
    #list_display = ('pergunta', 'data_pub', 'boo_ativo',)
    inlines = [EscolhaInline]
    exclude = ('data_pub',)
    #list_filter = ['data_pub']
    #search_fields = ['pergunta']
    date_hierarchy = 'data_pub'
          
    class Media:
        model = Enquete

if Modulo.objects.filter(modulo = 'enquete'):
    admin.site.register(Enquete, EnqueteAdmin)
