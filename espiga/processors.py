#-*- coding: utf-8 -*-

from video.models import Video
from link.models import Link
from perfilinicial.models import Perfil
from publicidade.models import Publicidade
from enquete.models import Enquete, Escolha
from django.db import connection

def auth(request):
    auth = False
    if request.user.is_authenticated():
         auth = request.user
         user_perfil = Perfil.objects.get(user=auth)
    
    return locals()

def ultimo_video(request):
    #ultimo video
    ultimo_video = Video.objects.all()[:1]
    
    lista_imagem_video = ()
    
    
    for lv in ultimo_video:
        video = lv.vch_url.split(" ")
        idvideo = video[6].split("/")
        idfoto = idvideo[4][:-1]
        
        lista_imagem_video = lista_imagem_video + ((lv.int_idvideo, lv.vch_titulo , lv.img_foto, idfoto,),)
        
    return locals()

def publicidade(request):
    #publicidade
    publicidade_topo = Publicidade.objects.filter(tipo="1")
    publicidade_direita = Publicidade.objects.filter(tipo="2")
    publicidade_rodape = Publicidade.objects.filter(tipo="3")
    publicidade_esquerda = Publicidade.objects.filter(tipo="4")
    publicidade_full_banner = Publicidade.objects.filter(tipo="5")
    
    return locals()

def enquete(request):
    #enquete
    ultima_enquete = Enquete.objects.latest("id_enquete") 
    enquete_esolhas = Escolha.objects.filter(enquete=ultima_enquete)
    
    return locals()

def links(request):
     #lista Links
    
    link_servico_destaque = Link.objects.filter(boo_destaque=True).filter(categoria=3)[:6]# para servicos
    link_rapidos = Link.objects.filter(categoria=4) #links rapidos
    link_rapidos_destaque = Link.objects.filter(categoria=1) #links rapidos destaque
    
    return locals()

