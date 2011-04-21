# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from perfilinicial.views import perfil

urlpatterns = patterns('',
    (r'^editarperfil/', 'perfilinicial.views.perfil'),
    

)