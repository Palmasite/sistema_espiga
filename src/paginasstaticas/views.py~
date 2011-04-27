# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from paginasstaticas.models import Pagina, Categoria




def pagina(request,url_categoria, url = None):
    
    if not url:
        pagina = get_object_or_404(Categoria, url = url_categoria)
        return render_to_response('default.html', locals(), context_instance=RequestContext(request))
    
    pagina = get_object_or_404(Pagina, url = url)
    return render_to_response('default.html', locals(), context_instance=RequestContext(request))
    
    

