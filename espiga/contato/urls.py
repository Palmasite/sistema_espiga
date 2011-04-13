from django.conf.urls.defaults import *
from contato.views import contato


urlpatterns = patterns('',
                       (r'^contato/$', 'contato.views.contato'),
                       )

