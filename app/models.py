from django.db import models
from django.contrib.auth.models import User
from itertools import *


# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    sinopsis = models.TextField(null=True)
    anio = models.IntegerField(null=True)
    actores=models.TextField(max_length=2000, null=True)
    duracion = models.IntegerField(null=True)
    enCartelera=models.BooleanField(null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.TextField(null=True)
    
 
    def __str__(self):
        return self.titulo
        
    class Meta:
        app_label = 'app'

class Categoria(models.Model):
    nombre = models.CharField(max_length=45, null=False)
    peliculas = models.ManyToManyField(Pelicula, related_name='peliculas')
    
    def __str__(self):
        return self.nombre
 
    class Meta:
        app_label = 'app'

class Calificacion(models.Model):
    valor = models.IntegerField(null=True)
    pelicula =models.ForeignKey(
        Pelicula,
        related_name='calificaciones',
        null=True,
        on_delete=models.PROTECT)
    usuario =models.ForeignKey(
        User,
        related_name='calificaciones',
        null=True,
        on_delete=models.PROTECT)

    def porcentaje(self):
        resultado = (self.valor*100) / 5
        return resultado
       
    class Meta:
        app_label = 'app'

class Comentario(models.Model):
    texto=models.TextField(max_length=2000, null=False)
    fechaHora = models.DateTimeField(auto_now_add=True)
    activo=models.BooleanField(null=False)
    pelicula =models.ForeignKey(
        Pelicula,
        related_name='comentarios',
        null=True,
        on_delete=models.PROTECT)
    usuario =models.ForeignKey(
        User,
        related_name='comentarios',
        null=True,
        on_delete=models.PROTECT)

    def __str__(self):
        return self.valor
 
    class Meta:
        app_label = 'app'







