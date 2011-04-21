#Create your views here

from agenda.models import Agenda, Eventos
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def eventos(request):
    
    eventos = Eventos.objects.all();
    
    return render_to_response('agenda.html',locals(), context_instance=RequestContext(request))

def evento(request,eventos_id):
    evento = Eventos.objects.get(pk = eventos_id)
    
    if request.is_ajax():
        html = "<p>f asdf asd</p>"
        return html
        
    
    return render_to_response('evento.html',locals(),context_instance=RequestContext(request))
    