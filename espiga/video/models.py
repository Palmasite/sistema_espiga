#-*- coding: utf-8 -*-
from django.db import models
import os
from django.conf import settings
from datetime import datetime
from thumbs import ImageWithThumbsField
from django import forms

""" Model video """
class Video(models.Model):    
    int_idvideo = models.AutoField(primary_key=True)
    vch_titulo = models.CharField("Nome video", max_length=500)
    vch_url = models.CharField("URL video", max_length=500, help_text=u"Preferência no tamanho do vídeo 853 X 510.",)
    dat_dataenvio = models.DateTimeField("Data Envio", default=datetime.now())
    boo_ativo = models.BooleanField("Ativo", default=True)
    img_foto = ImageWithThumbsField("Foto", upload_to='fotovideo/', sizes=((143, 87),), null=True, blank=True,)
    
    def save(self, force_insert=False, force_update=False):
        super(Video, self).save(force_insert, force_update)
          
        foto = str(self.img_foto)
        if foto != '':        
            f = str(foto).split('.') 
            """ Renomeia img_foto"""
            if not "368x278" in f:    
                self.img_foto = f[0] + '.143x87.' + f[1]
                os.remove(settings.MEDIA_ROOT + '/' + foto)
                        
            super(Video, self).save(force_insert, force_update)
            """ Apaga a foto original da pasta """
            
        else:
            super(Video, self).save(force_insert, force_update)
            
    def foto(self):
        foto = str(self.img_foto)
    
        img = '<img src="/espiga/media/' + foto + '"/>'       
        return img

    foto.allow_tags = True                 
      
        
    
    def __unicode__(self):
        return unicode(self.vch_titulo)
            
    class Meta:
        verbose_name = u'Video'
        verbose_name_plural = u'Videos'
        
