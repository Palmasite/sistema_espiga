# -*- coding: utf-8 -*-
from django.contrib.admin.options import ModelAdmin, TabularInline
from django.http import HttpResponseRedirect
from django.db.models.fields import FieldDoesNotExist
from django import forms
from django.db import models
from datetime_fields import DateWidget, DATE_INPUT_FORMAT
from django.contrib.admin.sites import AdminSite
#from autenticacao.models import TarefaAgendada, TAREFA_TIPO_ALTERA_SENHA

class MeuTabularInline(TabularInline):
    def get_form(self, request, obj=None, **kwargs):
        form = super(MeuTabularInline, self).get_form(request, obj=None, **kwargs)

        # Define campos e seus novos tipos e widgets para a realidade brasileira
        change_form_fields(form)

        return form

class MeuModelAdmin(ModelAdmin):
    def __init__(self, *args, **kwargs):
        super(MeuModelAdmin, self).__init__(*args, **kwargs)
      

    def get_form(self, request, obj=None, **kwargs):
        form = super(MeuModelAdmin, self).get_form(request, obj=None, **kwargs)

        # Define campos e seus novos tipos e widgets para a realidade brasileira
        change_form_fields(form)

        return form

class MeuAdminSite(AdminSite):
    def index(self, request):
       '''request.user.message_set.create(
                message=u'Olá, seja bem-vindo, %s!'%request.user.username,
                )'''

       resp = super(MeuAdminSite, self).index(request)

       return resp

    def login(self, request):
        resp = super(MeuAdminSite, self).login(request)

        if request.method == 'POST' and isinstance(resp, HttpResponseRedirect) and\
           TarefaAgendada.objects.filter(
                   usuario=request.user,
                   tipo=TAREFA_TIPO_ALTERA_SENHA,
                   ).count():
            request.user.message_set.create(message=u'Este é o seu primeiro logon. Altere sua senha.')
            return HttpResponseRedirect('/portal/pmp2010/password_change/')

        return resp

    def password_change_done(self, request):
        TarefaAgendada.objects.filter(
                   usuario=request.user,
                   tipo=TAREFA_TIPO_ALTERA_SENHA,
                   ).delete()

        resp = super(MeuAdminSite, self).password_change_done(request)

        return resp

def change_form_fields(form):
    if not hasattr(form, 'base_fields'):
        return form

    # Muda comportamento de alguns tipos de campo
    for field_name, field in form.base_fields.items():
        
        # Campos de data
        if isinstance(field, forms.DateField):
            field.input_formats = (DATE_INPUT_FORMAT,)
            field.widget = DateWidget()


    return form

from django.conf import settings
# Força os formatos de data para utilizar os definidos pelas settings
def force_date_formats():
    # Declarar settings DATE_FORMAT e DATETIME_FORMAT
    # Chamar este método no urls.py
    from django.utils import translation
    translation.get_date_formats = lambda: (settings.DATE_FORMAT, settings.DATETIME_FORMAT, settings.TIME_FORMAT)



