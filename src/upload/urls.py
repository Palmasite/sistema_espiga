from django.conf.urls.defaults import *
from upload.views import *


urlpatterns = patterns('',
    (r'^arquivos/$', 'upload.views.arquivos'),
    (r'^arquivos/(?P<idgaleria>\d+)/(?P<nome_galeria>\w+)/$', 'upload.views.arquivos'),
    

)
