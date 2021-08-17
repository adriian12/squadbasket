from django.shortcuts import render
from django.utils import timezone
from .models import  Noticia, Slider, Columna, Directiva, Equipo, Club, Organizacion, Plantilla, Jugadores, Entrenadores, Precio

# ------------------- Internas -----------------------

def home(request):
    slide = Slider.objects.all()
    columnas = Columna.objects.all()
    recientes = Noticia.objects.all()[:5]
    return render(request, 'index.html', {
        'columnas': columnas, 'slide': slide, 'recientes': recientes
    })

def club(request):
    club = Club.objects.all()
    org = Organizacion.objects.all()
    miembros = Directiva.objects.all()
    return render(request, 'club.html', {
        'club': club, 'org': org, 'miembros': miembros
    })

def contacto(request):
    return render(request, 'contacto.html', {})

def equipos(request):
    equipo = Equipo.objects.all()
    return render(request, 'equipos.html', {'equipo': equipo})

def plantillas(request):
    plantilla = Plantilla.objects.all()
    jugadores = Jugadores.objects.all()
    entrenadores = Entrenadores.objects.all()
    return render(request, 'plantilla.html', {'plantilla': plantilla, 'jugadores': jugadores, 'entrenadores': entrenadores})

def precios(request):
    precio = Precio.objects.all()
    return render(request, 'precios.html', {'precio': precio})

# def resultados(request):
#     return render(request, 'resultados.html', {})

def noticias(request):
    posts = Noticia.objects.all()
    return render(request, 'noticias.html', {'posts': posts})

def noticia_completa(request):
    completa = Noticia.objects.all()[:1]
    return render(request, 'noticias/noticia.html', {'completa': completa})

def politica(request):
    return render(request, 'politica.html', {})

def terminos(request):
    return render(request, 'terminos.html', {})

def enviar(request):
    return render(request, 'enviar.php', {})