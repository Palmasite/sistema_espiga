# -*- coding:utf-8 -*-

from django.forms.models import ModelForm
from perfilinicial.models import Perfil
from django.forms.fields import IntegerField
from django.forms.widgets import HiddenInput

class PerfilForm(ModelForm):
    #user = IntegerField(required=True,widget=HiddenInput())
    
    class Meta:
        model = Perfil  



