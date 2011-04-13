#Create your views here

from bancoimagem.models import Galeria, BancoImagem
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

'''def bancoimagem(request):
    bancoimagem = BancoImagem.objects.order_by('dat_foto')#[:5]
    paginator = Paginator(bancoimagem, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        imagens = paginator.page(page)
    except EmptyPage, InvalidPage:
        imagens = paginator.page(paginator.num_pages)

    return render_to_response('galeria.html',{'bancoimagem':imagens},context_instance=RequestContext(request))

'''

def galeria(request):
    lista_galeria = Galeria.objects.all()
    lista_imagem = BancoImagem.objects.all()
    return render_to_response('galeria.html',locals(), context_instance=RequestContext(request))

def imagem_aleria(request,idgaleria):
    lista_imagem = BancoImagem.objects.filter(galeria = idgaleria)
    galeria = BancoImagem.objects.filter(galeria = idgaleria)[:1]
    #galeria = imagem.galeria.descricao
    return render_to_response('imagem_galeria.html',locals(),context_instance=RequestContext(request))
    