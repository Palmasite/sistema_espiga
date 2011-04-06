from django.shortcuts import render_to_response
from django.template import RequestContext
from video.models import Video


def galeria_video(request, video_id):	
    video = Video.objects.filter(int_idvideo = video_id)  
    lista_video = Video.objects.all()      
    return render_to_response('video.html', locals(), context_instance=RequestContext(request))
