from django.db import models
from cliente.models import Local
# Create your models here.

class Cancion(models.Model):
	id = models.AutoField(primary_key=True)
	local = models.ForeignKey(Local, unique=False)
	nombre = models.CharField("Nombre de la cancion", max_length=150)
	directorio = models.CharField("Directorio de la cancion", max_length=150)
	album = models.CharField("Nombre del album", max_length=150)
	artista = models.CharField("Nombre del artista", max_length=150)
	duracion = models.TimeField()
	reproducciones = models.IntegerField("Reproducciones de la cancion",default=0)
	def __str__(self):
		return self.nombre