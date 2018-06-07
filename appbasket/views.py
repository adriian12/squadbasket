from django.shortcuts import render
from django.utils import timezone
from .models import Noticia, Slider, Columna, Reciente, Directiva

# ------------------- Internas -----------------------

def home(request):
    slide = Slider.objects.all()
    columnas = Columna.objects.all()
    recientes = Reciente.objects.all()
    miembros = Directiva.objects.all()
    return render(request, 'index.html', {
        'columnas': columnas, 'slide': slide, 'recientes': recientes, 'miembros': miembros
    })

def about(request):
    return render(request, 'about.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def equipos(request):
    return render(request, 'equipos.html', {})

def precios(request):
    return render(request, 'precios.html', {})

def resultados(request):
    return render(request, 'resultados.html', {})

# ----------------- Modulos --------------------------

def noticia_list(request):
    posts = Noticia.objects.all()
    return render(request, 'noticias.html', {'posts': posts})



