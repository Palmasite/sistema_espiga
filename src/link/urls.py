from django.conf.urls.defaults import *
from link.views import todos_servicos


urlpatterns = patterns('',
    (r'^maisservicos/', 'link.views.todos_servicos'),
                       

)
