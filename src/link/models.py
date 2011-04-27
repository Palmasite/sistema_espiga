# -*-ecoding:utf-8 -*-

from django.db import models
from thumbs import ImageWithThumbsField
from django.conf import settings
import os

# Create your models here.

class Categoria(models.Model):
    int_idcategoria = models.AutoField(primary_key=True)
    vch_titulo = models.CharField("Categoria", max_length = 250)
    def __unicode__(self):
        return self.vch_titulo
    class Meta:
        verbose_name = "Categoria"


class Link(models.Model):
    int_link = models.AutoField(primary_key=True)
    vch_nome = models.CharField(u'Nome que aparecerá no texto', max_length=100, blank=False, null=False)
    vch_link = models.CharField(u'Link', max_length=200, help_text='(AVISO: O Campo Link dever ser iniciado com http://)')
    img_foto = ImageWithThumbsField(verbose_name = "Logomarca", upload_to = "fotolink", sizes = ((200,237),),null = True, blank = True, )
    boo_destaque = models.BooleanField("Destaque", default=False)
    categoria = models.ForeignKey(Categoria)
    
    def save(self, force_insert=False, force_update=False):
            super(Link, self).save(force_insert, force_update)
            foto = str(self.img_foto)
            if foto != '':        
                f = str(foto).split('.') 
                """ Renomeia img_foto"""
                if not "200x237" in f:    
                    self.img_foto = f[0]+'.200x237.'+f[1]
                os.remove(settings.MEDIA_ROOT+'/'+foto)
                            
                super(Link, self).save(force_insert, force_update)
                """ Apaga a foto original da pasta """
                
            else:
                super(Link, self).save(force_insert, force_update)    
    
    def __unicode__(self):
        return unicode(self.vch_nome)
    class Meta:
        verbose_name = "Outro link "
        verbose_name_plural = "Link´s"