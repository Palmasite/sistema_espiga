# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

""" Model Enquete """
class Enquete(models.Model):
    id_enquete = models.AutoField(primary_key = True)
    pergunta = models.CharField(max_length = 200)
    data_pub = models.DateField('Data de Criação', default = datetime.now())
    boo_ativo = models.BooleanField('Ativo',default = True)

    def __unicode__(self):
        return self.pergunta
    class Meta:
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"
        
""" Model Escolha """
class Escolha(models.Model):
    id_escolha = models.AutoField(primary_key = True)
    enquete = models.ForeignKey(Enquete)
    escolha = models.CharField(max_length = 200)
    votos = models.IntegerField(default = 0, null = True, blank = True)
    
    def __unicode__(self):
        return self.escolha
    class Meta:
        verbose_name = "Escolha"
        verbose_name_plural = "Escolhas"
