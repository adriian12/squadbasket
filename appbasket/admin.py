from django.contrib import admin
from .models import Noticia, Slider, Columna, Reciente, Directiva, GaleriaEquipo, ClubInfo, ClubOrg, Plantilla, Datos

admin.site.register(Noticia)
admin.site.register(Slider)
admin.site.register(Columna)
admin.site.register(Reciente)
admin.site.register(Directiva)
admin.site.register(GaleriaEquipo)
admin.site.register(ClubOrg)
admin.site.register(Datos)



class ClubInfoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'descripcion', 'que_hacemos')
    prepopulated_fields = {}
    fieldsets = [
        (u'Quienes somos', {'fields': ('titulo', 'imagen', 'descripcion')}),
        (u'Que hacemos', {'fields': ('que_hacemos',)})
    ]

admin.site.register(ClubInfo, ClubInfoAdmin)


class DatosInline(admin.StackedInline):
    model = Datos
    extra = 3


class PlantillaAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['equipo']}),
        ('Jugador/a', {'fields': ['id', 'nombre', 'apellido', 'posicion', 'numero', 'imagen'],
                              'classes': ['collapse']}),
    ]

admin.site.register(Plantilla, PlantillaAdmin)
