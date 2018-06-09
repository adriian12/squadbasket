from django.conf.urls import include, url
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^equipos/$', views.equipos, name='equipos'),
    url(r'^precios/$', views.precios, name='precios'),
    url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^noticias/$', views.noticia_list, name='noticias'),
    url(r'^plantillas/$', views.plantillas, name='plantillas'),

]
