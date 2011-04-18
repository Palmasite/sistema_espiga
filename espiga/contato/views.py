# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from contato.forms import FormContato
from django.core.mail import send_mail
from contato.models import DadosEmpresa


def contato(request):
    
    dados_empresa = DadosEmpresa.objects.all()
    
    
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            form.save()
            form.enviar()
            mostrar = 'Contato enviado com sucesso.'
    else:
        form = FormContato()
    return render_to_response('contato.html', locals(), context_instance=RequestContext(request))