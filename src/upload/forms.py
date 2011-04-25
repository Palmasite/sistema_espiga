#-*- coding: utf-8 -*-
from django.forms import ModelForm
from upload.models import Arquivo
from django import forms
from datetime import datetime
from django.forms.widgets import *

#Vari�vel para formato de data
DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'
DATE_FORMAT = '%d/%m/%Y'

#widget para exibir data
class FormattedDateTimeInput(forms.DateTimeInput):
    format = DATETIME_FORMAT

class FormattedDateInput(forms.DateTimeInput):
    format = DATE_FORMAT


class ArquivoForm(ModelForm):
    dat_publicacao = forms.DateField(label=u"Data de Publicação", input_formats=[DATE_FORMAT], widget=FormattedDateInput(), help_text="Formato: dd/mm/aaaa")
    txt_resumo = forms.CharField(label="Resumo", required=False, widget=TextInput(attrs={'rows':'20'},), help_text="Digite o nome do titular")

    def clean_vch_arquivo(self):
		vch_arquivo = self.cleaned_data['vch_arquivo']
		extensao = str(vch_arquivo).split('.')[-1]
		if (extensao == "gif" or extensao == "jpg" or extensao == "jpeg" or extensao == "bmp" or extensao == "png" or
		    extensao == "GIF" or extensao == "JPG" or extensao == "JPEG" or extensao == "BMP" or extensao == "PNG"):
			raise forms.ValidationError(u'Não é permitido arquivos do tipo imagem!')
		return self.cleaned_data['vch_arquivo']

    class Meta:
		model = Arquivo


		
