from django.contrib import admin

from cargobr.carga.models import Carga


class DisplayDate(admin.ModelAdmin):
    list_display = ['id', 'user', 'valor']
    ordering = ['valor']


admin.site.register(Carga, DisplayDate)