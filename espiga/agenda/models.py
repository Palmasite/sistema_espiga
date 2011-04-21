# -*- coding: utf-8 -*-
from django.db import models

class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    nome = models.CharField('nome', max_length=200 )
    descricao = models.CharField(u'Descrição', max_length=200 )
    def __unicode__(self):
        return unicode(self.nome)

class Eventos(models.Model):
    id_eventos = models.AutoField(primary_key=True)
    agenda = models.ForeignKey(Agenda)
    titulo = models.CharField('Titulo', max_length=200 )
    inicio = models.DateTimeField('De :')
    fim    = models.DateTimeField('Ate:')
    local =  models.CharField('Local', max_length=200 )
    descricao = models.TextField(u'Descrição',null=True, blank=True)
    url = models.URLField("url",blank=True)
    todo_dia = models.BooleanField("Todo Dia")
    
    def __unicode__(self):
        return unicode(self.titulo)
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"