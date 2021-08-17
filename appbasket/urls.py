from django.conf.urls import include, url
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^club/$', views.club, name='club'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^equipos/$', views.equipos, name='equipos'),
    url(r'^precios/$', views.precios, name='precios'),
    # url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^plantillas/$', views.plantillas, name='plantillas'),
    url(r'^noticia/$', views.noticia_completa, name='noticia'),
    url(r'^politica/$', views.politica, name='politica'),
    url(r'^terminos/$', views.terminos, name='terminos'),  
]
