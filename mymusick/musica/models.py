from django.db import models
from cliente.models import Local
# Create your models here.

class Cancion(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField("Nombre de la cancion", max_length=150)
	directorio = models.CharField("Directorio de la cancion", max_length=150)
	duracion = models.TimeField()
	reproducciones = models.IntegerField("Reproducciones de la cancion",default=0)
	def __str__(self):
		return nombre


class Album(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField("Nombre del album", max_length=50)
	reproducciones = models.IntegerField("Reproducciones del album",default=0)
	canciones = models.ManyToManyField(Cancion)
	def __str__(self):
		return nombre

class Artista(models.Model):
	id = models.AutoField(primary_key=True)
	local = models.ForeignKey(Local, unique=False)
	nombre = models.CharField("Nombre del artista", max_length=50)
	reproducciones = models.IntegerField("Reproducciones del artista",default=0)
	albumes = models.ManyToManyField(Album)
	def __str__(self):
		return nombre
