from django.contrib import admin
from link.models import Link
from configuracoes.models import Modulo
 
class LinkAdmin(admin.ModelAdmin):
    list_display = ('vch_nome','vch_link',)
    model = Link
    
if Modulo.objects.filter(modulo = 'link'):    
    admin.site.register(Link,LinkAdmin)
