# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from imagens import meu_storage, getattr_thumb_foto
import os
from thumbs import ImageWithThumbsField
from django.conf import settings



class Categoria(models.Model):
    int_idcategoria = models.AutoField(primary_key=True)
    vch_titulo = models.CharField("Categoria", max_length = 250)
    def __unicode__(self):
        return self.vch_titulo
    class Meta:
        verbose_name = "Categoria"
        
""" Funcao responsavel pela renomeacao da foto que sera inserida no banco """
def upload_to_foto(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('fotonoticia/', '%s%s'%(horario, extensao))

""" Model noticia """
class Noticia(models.Model):
    int_idnoticia = models.AutoField(primary_key=True)
    vch_titulo = models.CharField("Título Notícia", max_length = 250)
    img_foto = ImageWithThumbsField("Foto", upload_to = upload_to_foto, sizes = ((368,278),), null = True, blank = True, help_text="Por favor enviar imagens no formato paisagem.( Para não desconfigurar a apresentação no site )" )
    vch_fotografo = models.CharField("Fotógrafo", max_length = 250, null=True, blank=True, )
    txt_olho = models.TextField("Olho",max_length= 250, null=True, blank=True)
    txt_noticia = models.TextField("Notícia")
    vch_autor = models.CharField("Autor da Notícia", max_length = 250, null=True, blank=True, )
    boo_destaque = models.BooleanField("Destaque", default=False)
    dat_noticia = models.DateTimeField("Data Notícia", default = datetime.now)
    boo_ativo = models.BooleanField("Ativa", default=True)
    categoria = models.ForeignKey(Categoria)
    
    def save(self, force_insert=False, force_update=False):
        super(Noticia, self).save(force_insert, force_update)
        foto = str(self.img_foto)
        if foto != '':        
            f = str(foto).split('.') 
            """ Renomeia img_foto"""
            if not "368x278" in f:    
                self.img_foto = f[0]+'.368x278.'+f[1]
                os.remove(settings.MEDIA_ROOT+'/'+foto)
                        
            super(Noticia, self).save(force_insert, force_update)
            """ Apaga a foto original da pasta """
            
        else:
            super(Noticia, self).save(force_insert, force_update)
    
    #Função para retornar 'fotos/000.jpg' caso não tenha foto no diretório.
    #Autor: Felipe
    def foto(self):
        if str(self.img_foto)!='':
            foto_path = '%s/%s'%(str(settings.MEDIA_ROOT), str(self.img_foto))
            if os.path.exists(foto_path):
                return str(self.img_foto)
            return 'fotos/000.jpg'
        return str(self.img_foto)
        
    def __unicode__(self):
        return self.vch_titulo
    
    class Meta:
        ordering = ('-dat_noticia',)
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        
