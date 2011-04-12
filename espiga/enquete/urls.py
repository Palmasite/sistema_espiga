# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from noticia.views import *



urlpatterns = patterns('',
    #(r'^index/', 'index.views.index'),
    #(r'^noticias/(?P<num_noticia>\d+)', 'noticia.views.noticias'),
    #(r'^mais/(?P<secretaria_id>\d+)/$', 'noticia.views.mais_noticias'),
    (r'^votar/(?P<enquete_id>\d+)/$', 'enquete.views.votar'),
    (r'^relatorio/(?P<enquete_id>\d+)/$',"enquete.views.relatorio"),
    #(r'^buscar/$', 'noticia.views.buscar'),
    #(r'^buscadocumento/$', 'noticia.views.frmbusca_arquivo'),
    #(r'^buscalei/$', 'noticia.views.frmbusca_lei'),    
    #(r'^buscaarquivolei/$', 'noticia.views.busca_lei_arquivo')
)