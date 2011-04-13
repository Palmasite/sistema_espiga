# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from enquete.models import Enquete,Escolha

def votar(request, enquete_id):
    enquete = Enquete.objects.get(pk = enquete_id)
    
    if request.method == "POST" :
        escolha = Escolha.objects.get(pk = request.POST["escolha"])
        escolha.votos += 1
        escolha.save() 
    
    resposta = "<html><body><p>Parabens voce votou<p></body></html>"
    return HttpResponse(resposta)

def relatorio(request, enquete_id):
    escolha = Escolha.objects.filter(enquete__id_enquete__exact = enquete_id)
 
    resposta = "<html><body><p><p></body></html>"
    return HttpResponse(resposta) 
    




       
