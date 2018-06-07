from django.db import models
from django.utils import timezone


# class Home(models.Model):
#     autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     titulo = models.CharField(max_length=200)
#     texto = models.TextField(max_length=80)
#     creada = models.DateTimeField(default=timezone.now)
#     imagen = models.ImageField(upload_to='uploads/logo')


class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=400)
    creada = models.DateTimeField(default=timezone.now)
    publicada = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publicada = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Slider(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='slides')

    def __str__(self):
        return self.titulo

class Columna(models.Model):
    col_titulo = models.CharField(max_length=50)
    col_texto = models.TextField(max_length=200)

    def __str__(self):
        return self.col_titulo

class Reciente(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    texto = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='noticias')

    def __str__(self):
        return self.titulo

class Directiva(models.Model):
    nombre = models.CharField(max_length=30)
    puesto = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='directiva')

    def __str__(self):
        return self.nombre