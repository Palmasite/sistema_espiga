from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'espiga.views.home', name='home'),
    # url(r'^espiga/', include('espiga.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^index/', 'views.index'),
    (r'^logar$', 'views.logar'),
    (r'^logout/', 'views.sair'),
    (r'^recuperar_senha/$', 'password_reset', {'template_name': 'accounts/registration/password_reset_form.html', 'email_template_name':'accounts/registration/password_reset_email.html', 'post_reset_redirect':'accounts/login/'}), 
    
    
    (r'^noticia/', include('noticia.urls')),
    (r'^bancoimagem/', include('bancoimagem.urls')),
    (r'^enquete/', include('enquete.urls')),
    (r'^video/', include('video.urls')),
    (r'^contato/',include('contato.urls')),
    
)
