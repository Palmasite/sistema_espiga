# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from enquete.models import Enquete,Escolha


def relatorio(request):
    escolha = Escolha.objects.filter(enquete__id_enquete__exact = enquete_id)

    for opsao in escolha:
        resposta += "<span>"+opsao.escolha+" : <strong>"+opsao.votos+"</strong></span>"
    
    return HttpResponse(resposta) 

def votar(request):
    
    
    if request.method == "POST" :
        enquete_id = request.POST['enquete']
        enquete = Enquete.objects.get(pk = enquete_id)
        escolha = Escolha.objects.get(pk = request.POST["opsao"])
        escolha.votos += 1
        escolha.save()
    else :
        enquete_id = request.GET['enquete']
        enquete = Enquete.objects.get(pk = enquete_id)
        
    escolha = Escolha.objects.filter(enquete__id_enquete__exact = enquete_id)

    resposta = ''
    for opsao in escolha:
        resposta = resposta + "<span>"+opsao.escolha+" : "+str(opsao.votos)+" votos</span>"

    return HttpResponse(resposta)

       
