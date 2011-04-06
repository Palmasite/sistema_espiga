# -*-ecoding:utf-8 -*-

from django.db import models

# Create your models here.

class Link(models.Model):
    int_link = models.AutoField(primary_key=True)
    vch_nome = models.CharField(u'Nome que aparecerá no texto', max_length=100, blank=False, null=False)
    vch_link = models.CharField(u'Link', max_length=200, help_text='(AVISO: O Campo Link dever ser iniciado com http://)')
    
    def __unicode__(self):
        return unicode(self.vch_nome)
    
    class Meta:
        verbose_name = "Outro link "
        verbose_name_plural = "Link´s"