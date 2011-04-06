from django.db import models
from thumbs import ImageWithThumbsField
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User
import os



class Perfil(models.Model):

    #cargos = (('1','Prefeito'),('2','Vice-Prefeito'),('3','Primeira-Dama'),('4','Secretario de Governo'),('5','Assessor Parlamentar'),('6','Chefe de Gabinete'))
    int_idperfil = models.AutoField(primary_key=True)
    vch_nome = models.CharField("Nome", max_length = 250)
    user = models.ForeignKey(User)
    #int_cargo = models.IntegerField("Cargo", choices=cargos)
    img_foto = ImageWithThumbsField(verbose_name = "Foto ", upload_to = "foto", sizes = ((180,237),), null = True, blank = True,)
    #txt_curriculo = models.TextField("Curriculo",  )
    #txt_trajetoria = models.TextField("Trajetoria Politica", null=True, blank= True,)    

	
    
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
    
