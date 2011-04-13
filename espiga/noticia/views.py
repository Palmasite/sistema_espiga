# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from noticia.models import Noticia
from datetime import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils import simplejson
from django.http import HttpResponse


def mais_noticias(request):
    lista_mais_noticias = Noticia.objects.all().order_by('-dat_noticia')[:50]
    lista_noticias_mes = lista_mais_noticias.dates('dat_noticia', 'month').reverse()  
    return render_to_response('mais_noticias.html', locals(), context_instance=RequestContext(request))

def detalhar_noticia(request, noticia_id):
    noticia_detalhada = Noticia.objects.filter(int_idnoticia = noticia_id).order_by('dat_noticia')[:10]
    noticias_relacionadas = Noticia.objects.filter(categoria=noticia_detalhada[0].categoria).exclude(int_idnoticia=noticia_id).order_by('-dat_noticia')[:3]
    return render_to_response('noticiadetalhada.html', locals(), context_instance=RequestContext(request))

def buscar_noticia(request):
    
    parametro_busca = request.GET.get('buscar')
    
    if parametro_busca:
        lista_mais_noticias = Noticia.objects.filter(txt_noticia__icontains = parametro_busca).order_by('-dat_noticia')
        lista_noticias_mes = lista_mais_noticias.dates('dat_noticia', 'month').reverse()  
    else:
        lista_mais_noticias = Noticia.objects.all().order_by('-dat_noticia')[:50]
        lista_noticias_mes = lista_mais_noticias.dates('dat_noticia', 'month').reverse() 

    return render_to_response('mais_noticias.html', locals(), context_instance=RequestContext(request))

    
    
       
