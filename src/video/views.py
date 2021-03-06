from django.shortcuts import render_to_response
from django.template import RequestContext
from video.models import Video


def galeria(request):    
    lista_video = Video.objects.all()
    
    lista_imagem_video = ()
    
    for lv in lista_video:
        video = lv.vch_url.split(" ")
        idvideo = video[6].split("/")
        idfoto = idvideo[4][:-1]
        
        lista_imagem_video = lista_imagem_video + ((lv.int_idvideo, lv.vch_titulo , lv.img_foto, idfoto,),)
        
        
    #raise Exception(lista_imagem_video)
    
         
    return render_to_response('videos.html', locals(), context_instance=RequestContext(request))


def galeria_video(request, video_id):	
    video = Video.objects.filter(int_idvideo=video_id)    
    return render_to_response('iframe_video.html', locals(), context_instance=RequestContext(request))
