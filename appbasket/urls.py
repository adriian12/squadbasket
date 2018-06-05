from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^$', views.noticia_list),
    url(r'^$', views.slider_content),
]