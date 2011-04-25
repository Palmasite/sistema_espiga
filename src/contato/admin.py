from django.contrib import admin
from models import Departamento, Contato, DadosEmpresa
from configuracoes.models import Modulo
from django.conf import settings

class AdmiDadosEmpresa(admin.ModelAdmin):
    
    
    class Media:
        model = DadosEmpresa
        js = (settings.MEDIA_URL + "/js/editorHtml/jscripts/tiny_mce/tiny_mce.js", # insere o javascript do editor html na pagina
              settings.MEDIA_URL + "/js/editorHtml/textarea.js",)# insere o javascript do editor html na pagina


if Modulo.objects.filter(modulo='contato'):
    admin.site.register(Departamento)
    admin.site.register(Contato)
    admin.site.register(DadosEmpresa, AdmiDadosEmpresa)



