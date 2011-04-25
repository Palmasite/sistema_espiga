#-*- coding: utf-8 -*-
from django.db import models
import os
from django.conf import settings
from datetime import datetime
from django import forms


class Galeria(models.Model):
    idgaleria = models.AutoField(primary_key=True)
    descricao = models.CharField('Nome Galeria', max_length=500)
    
    def __unicode__(self):
        return unicode(self.descricao)
    class Meta:
        verbose_name = "Galeria de arquivo"
        verbose_name_plural = "Galeria de arquivos em geral"


def upload_to_arquivo(instance, name):
    pasta_galeria = str(instance.galeria.descricao)
    extensao = os.path.splitext(name)[-1]
    data = datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    #raise Exception(os.path.join('%s/'%(pasta_galeria),'%s%s'%(horario, extensao)))
    return os.path.join('upload/%s/' % (pasta_galeria), '%s%s' % (horario, extensao))
    #return os.path.join('galeria/', '%s%s'%(horario, extensao))



        
class Arquivo(models.Model):
    int_idarquivo = models.AutoField(primary_key=True)
    galeria = models.ForeignKey('Galeria')
    vch_titulo = models.CharField("Nome Arquivo", max_length=500)
    vch_arquivo = models.FileField("Arquivo", upload_to=upload_to_arquivo)
    dat_cadastro = models.DateTimeField("Data de Envio", default=datetime.now())
    char_tipo = models.BooleanField("Ativar Arquivo")
    dat_publicacao = models.DateField("Data de Publicação")
    txt_resumo = models.TextField("Resumo", max_length=500)
    

    def save(self):
        super(Arquivo, self).save()
        if self.vch_arquivo:
            pasta_galeria = str(self.galeria.descricao)
            arquivo = str(self.vch_arquivo)
            extensao = str(arquivo).split('.')[-1]
            data = datetime.now()
            horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
            self.vch_arquivo = "upload/%s/%s.%s" % (str(pasta_galeria), str(horario), extensao)
            if os.path.exists(settings.MEDIA_ROOT + '/' + arquivo):
                os.rename(settings.MEDIA_ROOT + '/' + arquivo, settings.MEDIA_ROOT + '/' + str(self.vch_arquivo))
            else:
                self.vch_arquivo = "erro"
        super(Arquivo, self).save()
    def __unicode__(self):
        return unicode(self.vch_titulo)
    
    class Meta:
        verbose_name = u'Arquivo'
        verbose_name_plural = u'Arquivos'

        

        
