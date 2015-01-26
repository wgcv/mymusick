from django.db import models
from musica.models import Cancion
from cliente.models import Local
# Create your models here.

class Lista(models.Model):
	id = models.AutoField(primary_key=True)
	local = models.ForeignKey(Local, unique=True)
	canciones = models.ManyToManyField(Cancion)
	def __str__(self):
		return self.local.nombre

		