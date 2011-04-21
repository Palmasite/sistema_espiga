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
from noticia.models import Noticia
from enquete.models import Enquete, Escolha
from publicidade.models import Publicidade
from django.contrib.auth import authenticate, login,logout
from django.contrib.redirects.models import Redirect
from urllib2 import HTTPRedirectHandler
from django.core import serializers
from django.utils import simplejson

from link.models import Link, Categoria

def index(request):
    #verifica se ta authenticado
    if request.user.is_authenticated():
         auth = request.user
         
    #lista de noticias       
    outras_noticias  = Noticia.objects.filter(boo_ativo = True)[:4]
    
    #lista galeria
    lista_galeria = Galeria.objects.all()[:3]
    lista_imagem = BancoImagem.objects.all()
    
    #ultimo video
    ultimo_video = Video.objects.all()[:1]
    
    lista_imagem_video = ()
    
    for lv in ultimo_video:
        video = lv.vch_url.split(" ")
        idvideo = video[6].split("/")
        idfoto=idvideo[4][:-1]
        
        lista_imagem_video = lista_imagem_video + ((lv.int_idvideo,lv.vch_titulo ,lv.img_foto,idfoto,),)
        
    
    
    
    
    
    #publicidade
    publicidade_topo = Publicidade.objects.filter(tipo = "1")
    publicidade_direita = Publicidade.objects.filter(tipo = "2")
    publicidade_rodape = Publicidade.objects.filter(tipo = "3")
    publicidade_esquerda = Publicidade.objects.filter(tipo = "4")
    publicidade_full_banner = Publicidade.objects.filter(tipo = "5")
    
    #noticias_destque
    noticias_destaque = Noticia.objects.filter(boo_ativo = True).filter(boo_destaque = True);
    #enquete
    ultima_enquete = Enquete.objects.latest("id_enquete") 
    enquete_esolhas =  Escolha.objects.filter(enquete = ultima_enquete)
    
    #lista Links
    
    link_servico_destaque = Link.objects.filter(boo_destaque = True).filter(categoria = 3)[:6]# para servicos
    link_rapidos = Link.objects.filter(categoria = 4) #links rapidos
    link_rapidos_destaque = Link.objects.filter(categoria = 1) #links rapidos destaque
    
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def logar(request):
    
    mimetype = 'application/javascript'  
    
    user = request.POST['username']
    passw = request.POST['password']
    message = ""        
    user_login = authenticate(username=user, password=passw)    
    if user_login is not None:
        if user_login.is_active:
            retorno = {'status':'ok','message':'<span>Seja bem vindo : <strong>'+user_login.username+'</strong></span>'}
            login(request,user_login)
        else:
            retorno = {'status':'no','message':'<span style="color:#A20000">usario não ativo<span>'}
    else:
        retorno ={'status':'no','message':'<span style="color:#A20000">Usuário ou senha inválido<span>'}
    
    return HttpResponse(simplejson.dumps(retorno),mimetype)

def sair(request):
    logout(request)
    return redirect('/index')