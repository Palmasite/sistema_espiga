# -*-ecoding:utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from django.conf import settings

from django.contrib.auth.models import User
import os

class Perfil(models.Model):
    int_idperfil = models.AutoField(primary_key=True)
    vch_nome = models.CharField("Nome", max_length = 250)
    vch_cargo = models.CharField("Cargo", max_length = 250)
    vch_area = models.CharField(u"Área", max_length = 250)
    matricula = models.CharField("Matricula", max_length = 250)
    user = models.ForeignKey(User)
    img_foto = ImageWithThumbsField(verbose_name = "Foto ", upload_to = "foto", sizes = ((180,237),), null = True, blank = True,)
    
    def save(self, force_insert=False, force_update=False):
        super(Perfil, self).save(force_insert, force_update)
        foto = str(self.img_foto)
        if foto != '':        
            f = str(foto).split('.') 
            """ Renomeia img_foto"""
            if not "180x237" in f:    
                self.img_foto = f[0]+'.180x237.'+f[1]
                os.remove(settings.MEDIA_ROOT+'/'+foto)
                        
            super(Perfil, self).save(force_insert, force_update)
            """ Apaga a foto original da pasta """
            
        else:
            super(Perfil, self).save(force_insert, force_update)
        
    def __unicode__(self):
        return unicode(self.vch_nome)
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"



class Profissional(models.Model):
    list_tipo = (('1',u'Profissão'),('2',u'Especialização'))    
    int_idprofissao = models.AutoField(primary_key=True)
    vch_formacao = models.CharField(u"Formação", max_length = 250)
    vch_instituicao = models.CharField(u"Instituição", max_length = 250)
    vch_local = models.CharField("Local", max_length = 250)
    vch_tipo = models.CharField("Tipo", max_length = 2, choices = list_tipo)    
    perfil = models.ForeignKey(Perfil)
    
    def __unicode__(self):
        return unicode(self.vch_formacao)

class Contato(models.Model):
    list_tipo = (('1','Fone/Ramal'),('2','Cel. trabalho'),('3','Cel. pessoal'),('4','Email trabalho'),('5','Email pessoal'),)
    int_idcontato = models.AutoField(primary_key=True)
    vch_contato = models.CharField("Contato", max_length = 250)
    vch_tipo = models.CharField("Tipo", max_length = 2, choices = list_tipo)    
    perfil = models.ForeignKey(Perfil)
    
    def __unicode__(self):
        return unicode(self.vch_contato)
    
    
class RedeSocial(models.Model):
    list_tipo = (('1','Orkut'),('2','Facebook'),('3','MSN'))  
    int_idcontato = models.AutoField(primary_key=True)
    rede = models.CharField("Contato", max_length = 250)
    vch_tipo = models.CharField("Tipo", max_length = 2, choices = list_tipo)    
    perfil = models.ForeignKey(Perfil)