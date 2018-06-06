from django.shortcuts import render
from django.utils import timezone
from .models import Noticias, Slider, Columnas

# ------------------- Internas -----------------------

def home(request):
    return render(request, 'index.html', {})

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
    posts = Noticias.objects.all()
    return render(request, 'noticias.html', {'posts': posts})

def slider_content(request):
    slide = Slider.objects.all()
    return render(request, 'slider.html', {'slide': slide})

def columna_list(request):
    columnas = Columnas.objects.all()
    return render(request, 'index.html', {'columnas': columnas})
    print columna_list



