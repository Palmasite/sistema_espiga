# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from imagens import meu_storage, getattr_thumb_foto
import os
from thumbs import ImageWithThumbsField
from django.conf import settings


class Galeria(models.Model):
    idgaleria = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=200, )
    descricao = models.CharField(u'Descrição', max_length=500, null=True, blank=True)
    
    
    def __unicode__(self):
        return unicode(self.descricao)
    class Meta:
        verbose_name = "Galeria de imagem"
        verbose_name_plural = "Galeria de imagens"

""" Funcao resposalvel pela renomeacao da foto que sera inserida no banco """
'''def upload_to_foto(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('galeria/', '%s%s'%(horario, extensao))'''


def upload_to_foto(instance, name):
    pasta_galeria = str(instance.galeria.descricao)
    extensao = os.path.splitext(name)[-1]
    nome = os.path.splitext(name)[0]
    data = datetime.now()
    horario = str(nome)+"-"+str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    #raise Exception(os.path.join('%s/'%(pasta_galeria),'%s%s'%(horario, extensao)))
    return os.path.join('galeria/%s/'%(pasta_galeria),'%s%s'%(horario, extensao))
    #return os.path.join('galeria/', '%s%s'%(horario, extensao))

class BancoImagem(models.Model):
    ModuloNoticia = 1
    int_idbancoimagem = models.AutoField(primary_key = True)
    vch_titulo = models.CharField("Título Foto", max_length = 250)
    img_foto = ImageWithThumbsField(verbose_name = "Foto", upload_to = upload_to_foto, sizes = ((150,85),(800,600)))
    img_miniatura = models.CharField(max_length = 100, null = True, blank = True)
    dat_foto = models.DateTimeField("Data Foto", default = datetime.now)
    vch_fotografo = models.CharField("Fotógrafo", max_length = 250, null = True, blank = True)
    capa_album = models.BooleanField("Capa do album")
    
    galeria = models.ForeignKey('Galeria')
    def save(self):
        super(BancoImagem, self).save()
        
        foto = str(self.img_foto)        
        f = str(foto).split('.')  
        """ Renomeia img_foto"""    
        self.img_foto = f[0]+'.800x600.'+f[1]
        """ Renomeia img_miniatura"""    
        self.img_miniatura = f[0]+'.150x85.'+f[1]
        super(BancoImagem, self).save()
        """ Apaga a foto original da pasta """
        os.remove(settings.MEDIA_ROOT+'/'+foto)
    
    """ funcao que coloca as imagens no campo img_foto na consulta """
    def foto(self):
        foto = str(self.img_miniatura)
    
        img = '<img src="/espiga/media/'+foto+'"/>'       
        return img

    foto.allow_tags = True 
   
    def __unicode__(self):
        return self.vch_titulo
    
    class Meta:
        verbose_name = "Banco de Imagem"
        verbose_name_plural = "Banco de Imagem"


""" Model banco de imagem """
'''class BancoImagem(models.Model):
    ModuloNoticia = 1
    int_idbancoimagem = models.AutoField(primary_key = True)
    vch_titulo = models.CharField("Título Foto", max_length = 250)
    img_foto = ImageWithThumbsField(verbose_name = "Foto", upload_to = upload_to_foto, sizes = ((72,72),(620,317)))
    img_miniatura = models.CharField(max_length = 100, null = True, blank = True)
    dat_foto = models.DateTimeField("Data Foto", default = datetime.now)
    vch_fotografo = models.CharField("Fotógrafo", max_length = 250, null = True, blank = True)
    galeria = models.ForeignKey('Galeria')
    def save(self):
        super(BancoImagem, self).save()
        
        foto = str(self.img_foto)        
        f = str(foto).split('.')  
        """ Renomeia img_foto"""    
        self.img_foto = f[0]+'.620x317.'+f[1]
        """ Renomeia img_miniatura"""    
        self.img_miniatura = f[0]+'.72x72.'+f[1]
        super(BancoImagem, self).save()
        """ Apaga a foto original da pasta """
        os.remove(settings.MEDIA_ROOT+'/'+foto)
    
    """ funcao que coloca as imagens no campo img_foto na consulta """
    def foto(self):
        foto = str(self.img_miniatura)
    
        img = '<img src="/espiga/media/'+foto+'"/>'       
        return img

    foto.allow_tags = True 
   
    def __unicode__(self):
        return self.vch_titulo
    
    class Meta:
        verbose_name = "Banco de Imagem"
        verbose_name_plural = "Banco de Imagem"'''
