# Create your views here.
from perfilinicial.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from perfilinicial.models import Perfil




from perfilinicial.forms import PerfilForm 


def perfil(request):
    
    if request.user.is_authenticated():
        try:
            perfil = Perfil.objects.get(user = request.user)
            formperfil = PerfilForm(instance=perfil)
            
        except:
            formperfil = PerfilForm(request.POST)
            
            if request.method == 'POST':
                form = PerfilForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    raise Exception('kkkkk')
            else:
                pass
    else:
        pass
        
    return render_to_response('perfil.html',locals(), context_instance=RequestContext(request))
