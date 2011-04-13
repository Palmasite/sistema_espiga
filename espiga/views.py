# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from datetime import datetime
from django.utils import simplejson
from django.http import HttpResponse
from noticia.models import Noticia
from bancoimagem.models import BancoImagem, Galeria
from video.models import Video
from enquete.models import Enquete, Escolha

def index(request):
    
    outras_noticias  = Noticia.objects.filter(boo_ativo = True)[:4]
    
    lista_galeria = Galeria.objects.all()[:3]
    lista_imagem = BancoImagem.objects.all()
    
    ultimo_video = Video.objects.all()[:1]
    
    ultima_enquete = Enquete.objects.latest("id_enquete")
    enquete_esolhas =  Escolha.objects.filter(enquete = ultima_enquete)
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

