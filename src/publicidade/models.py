# -*- ecoding: utf-8 -*-

from django.db import models
from thumbs import ImageWithThumbsField
from django.conf import settings 

import os

class Publicidade(models.Model):
    list_tipo = (('1', 'Topo'), ('2', 'Direita'), ('3', u'Rodapé'), ('4', 'Esquerda'), ('5', 'fullbanner'))
    idpublicidade = models.AutoField(primary_key=True)
    nome = models.CharField("Nome", max_length=250)
    img_foto = ImageWithThumbsField(verbose_name="Logomarca", upload_to="fotopublicidade", sizes=((180, 237),), null=True, blank=True,)
    tipo = models.CharField("Posição no portal", max_length=1, choices=list_tipo,)
    
    def save(self, force_insert=False, force_update=False):
            super(Publicidade, self).save(force_insert, force_update)
            foto = str(self.img_foto)
            if foto != '':        
                f = str(foto).split('.') 
                """ Renomeia img_foto"""
                if not "180x237" in f:    
                    self.img_foto = f[0] + '.180x237.' + f[1]
                os.remove(settings.MEDIA_ROOT + '/' + foto)
                            
                super(Publicidade, self).save(force_insert, force_update)
                """ Apaga a foto original da pasta """
                
            else:
                super(Publicidade, self).save(force_insert, force_update)
            
    def __unicode__(self):
        return unicode(self.nome)
    class Meta:
        verbose_name = "Publicidade"
        verbose_name_plural = "Publicidades"
        
    
