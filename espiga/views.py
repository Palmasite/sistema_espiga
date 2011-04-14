# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from datetime import datetime
from django.utils import simplejson
from django.http import HttpResponse
from noticia.models import Noticia
from bancoimagem.models import BancoImagem, Galeria
from video.models import Video
from enquete.models import Enquete, Escolha
from django.contrib.auth import authenticate, login,logout
from django.contrib.redirects.models import Redirect
from urllib2 import HTTPRedirectHandler

def index(request):
    #verifica se ta authenticado
    if request.user.is_authenticated():
         auth = request.user
             
    outras_noticias  = Noticia.objects.filter(boo_ativo = True)[:4]
    
    lista_galeria = Galeria.objects.all()[:3]
    lista_imagem = BancoImagem.objects.all()
    
    ultimo_video = Video.objects.all()[:1]
    
    ultima_enquete = Enquete.objects.latest("id_enquete")
    enquete_esolhas =  Escolha.objects.filter(enquete = ultima_enquete)
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def logar(request):    
    user = request.POST['username']
    passw = request.POST['password']        
    user_login = authenticate(user = user,password =passw)
    if request.is_ajax():    
        pass
    return HttpResponse(user)
            
def sair(request):
    logout(request)
    return redirect('/index')