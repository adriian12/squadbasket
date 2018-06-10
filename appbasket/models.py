from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode

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

    def __unicode__(self):
        return (u"%s" % self.titulo)

class Slider(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='slides')

    def __unicode__(self):
        return (u"%s" % self.titulo)

class Columna(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=250)
    icono = models.TextField(max_length=50)

    def __unicode__(self):
        return (u"%s" % self.titulo)

class Reciente(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    texto = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='noticias')

    def __unicode__(self):
        return (u"%s" % self.titulo)

class Directiva(models.Model):
    nombre = models.CharField(max_length=30)
    puesto = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='directiva')
    id = models.CharField(primary_key=True, max_length=25)
    tabla = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return (u"%s" % self.nombre)

class Equipo(models.Model):
    categoria = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='categorias')
    equipo = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, max_length=50)
    id = models.CharField(primary_key=True, max_length=25)

    def __unicode__(self):
        return (u"%s" % self.equipo)


class ClubInfo(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='club')
    descripcion = models.TextField( max_length=550)
    que_hacemos = models.TextField(max_length=500)

    def __unicode__(self):
        return (u"%s" % self.titulo)

class ClubOrg(models.Model):
    titulo = models.CharField(max_length=50)
    id = models.CharField(primary_key=True, max_length=25)
    descripcion = models.TextField(blank=True, max_length=300, default='org')

    def __unicode__(self):
        return (u"%s" % self.titulo)

class Plantilla(models.Model):
    id = models.CharField(primary_key=True, max_length=25)
    equipo = models.ForeignKey(Equipo)
    nombre = models.CharField(blank=True, max_length=30)

    def __unicode__(self):
        return (u"%s" % self.equipo)

class Jugadores(models.Model):
    equipo = models.ForeignKey(Plantilla)
    dorsal = models.CharField(blank=True, max_length=2)
    nombre = models.CharField(max_length=25 )
    apellido = models.CharField(blank=True, max_length=20)
    posicion = models.CharField(blank=True, max_length=15)
    id = models.CharField(primary_key=True, max_length=4)
    imagen = models.ImageField(upload_to='plantilla/', default='plantilla/default.jpeg', blank=True,)

class Entrenadores(models.Model):
    equipo = models.ForeignKey(Plantilla)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(blank=True, max_length=20)
    posicion = models.CharField(blank=True, max_length=15)
    id = models.CharField(primary_key=True, max_length=4)
    imagen = models.ImageField(upload_to='plantilla/', default='plantilla/default.jpeg', blank=True, )

class Precio(models.Model):
    categoria = models.CharField(max_length=25)
    total = models.CharField(max_length=20)
    complemento_uno = models.CharField(u'Complemento', blank=True, max_length=35)
    complemento_dos = models.CharField(u'Complemento', blank=True, max_length=35)
    complemento_tres = models.CharField(u'Complemento',blank=True,  max_length=35)
    complemento_cuatro = models.CharField(u'Complemento', blank=True, max_length=35)
    complemento_cinco = models.CharField(u'Complemento', blank=True, max_length=35)
    url = models.TextField(blank=True, max_length=150)

    def __unicode__(self):
        return (u"%s" % self.categoria)
