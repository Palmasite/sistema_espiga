from django.contrib import admin
from link.models import Link, Categoria

 
class LinkAdmin(admin.ModelAdmin):
    list_display = ('vch_nome','vch_link',)
    model = Link
    
admin.site.register(Link,LinkAdmin)
admin.site.register(Categoria)
