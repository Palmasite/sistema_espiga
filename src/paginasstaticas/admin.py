from django.contrib import admin
from paginasstaticas.models import Categoria, Pagina
from django.conf import settings

class AdminPagina(admin.ModelAdmin):
    
    class Media:
        model = Pagina
        js = (settings.MEDIA_URL + "/js/editorHtml/jscripts/tiny_mce/tiny_mce.js", # insere o javascript do editor html na pagina
              settings.MEDIA_URL + "/js/editorHtml/textarea.js",)# insere o javascript do editor html na pagina



admin.site.register(Pagina, AdminPagina)
admin.site.register(Categoria)
