#!/usr/bin/env python
import os, sys

dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(dir, '..'))
sys.path.insert(1, os.path.join(dir, '..', '..', 'dependencias'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

