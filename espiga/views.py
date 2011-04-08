# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from datetime import datetime
from django.utils import simplejson
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

