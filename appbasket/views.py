from django.shortcuts import render
from django.utils import timezone
from .models import Noticias
from .models import Slider


def home(request):
    return render(request, 'index.html', {})

def noticia_list(request):
    posts = Noticias.objects.all()
    return render(request, 'noticias.html', {'posts': posts})

def slider_content(request):
    slide = Slider.objects.all()
    return render(request, 'slider.html', {'slide': slide})