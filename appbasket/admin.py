from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Noticia, Slider, Columna, Reciente, Directiva, GaleriaEquipo, ClubInfo, ClubOrg, Plantilla, Jugadores

admin.site.register(Noticia)
admin.site.register(Slider)
admin.site.register(Columna)
admin.site.register(Reciente)
admin.site.register(Directiva)
admin.site.register(GaleriaEquipo)
admin.site.register(ClubOrg)



class ClubInfoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'descripcion', 'que_hacemos')
    prepopulated_fields = {}
    fieldsets = [
        (u'Quienes somos', {'fields': ('titulo', 'imagen', 'descripcion')}),
        (u'Que hacemos', {'fields': ('que_hacemos',)})
    ]

admin.site.register(ClubInfo, ClubInfoAdmin)


class JugadoresLista(admin.TabularInline):
    model = Jugadores
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 20})},
    }

class PlantillaAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['id', 'equipo']}),

    ]
    inlines = [JugadoresLista]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 20})},
    }

admin.site.register(Plantilla, PlantillaAdmin)
