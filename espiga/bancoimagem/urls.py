# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from bancoimagem.views import *

urlpatterns = patterns('',
    #(r'^galeria/', 'bancoimagem.views.bancoimagem'),
    (r'^galeria/', 'bancoimagem.views.galeria'),
    

)
