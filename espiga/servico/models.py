# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings 

# Create your models here.
class Servico(models.Model):
    int_idservico = models.AutoField(primary_key=True)
    vch_titulo = models.CharField("Titulo", max_length = 250)
    txt_servico = models.TextField(u"Serviço")
    boo_ativo = models.BooleanField("Ativa", default=True)

    vch_nome_servico_interno = models.CharField(u'Título do serviço interno', max_length=100, blank=True, null=True)
    vch_link_servico_interno = models.CharField(u'Link do serviço interno ', max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.vch_titulo)
    
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        
class LinkServico(models.Model):
    int_linkservico = models.AutoField(primary_key=True)
    servico = models.ForeignKey(Servico, verbose_name="Serviço")
    vch_nome = models.CharField(u'Nome que aparecerá no texto', max_length=100, blank=False, null=False)
    vch_link = models.CharField(u'Link', max_length=200)

    class Meta:
        verbose_name = "Outro link"
        verbose_name_plural = "Link´s do serviço (Caso o serviço a ser cadastrado tenha link´s associados, insira-os aqui. AVISO: O Campo Link dever ser iniciado com http://)"    