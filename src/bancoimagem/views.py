#Create your views here

from bancoimagem.models import Galeria, BancoImagem
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def galeria(request):
    lista_galeria = Galeria.objects.all()
    lista_imagem = BancoImagem.objects.all()
    return render_to_response('galeria.html', locals(), context_instance=RequestContext(request))

def imagem_aleria(request, idgaleria):
    lista_imagem = BancoImagem.objects.filter(galeria=idgaleria)
    galeria = BancoImagem.objects.filter(galeria=idgaleria)[:1]
    #galeria = imagem.galeria.descricao
    return render_to_response('imagem_galeria.html', locals(), context_instance=RequestContext(request))
    
