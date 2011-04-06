#-*- coding: utf-8 -*-
from django.contrib import admin
from configuracoes.models import Modulo, Layout



class LayoutAdmin(admin.ModelAdmin):
    list_display = ('topobg','topo','logo','menufundo',)
    model = Layout

admin.site.register(Layout,LayoutAdmin)
admin.site.register(Modulo)