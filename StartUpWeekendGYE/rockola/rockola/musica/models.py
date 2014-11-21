from django.db import models

# Create your models here.

class Musica(models.Model):
	nombre = models.CharField(max_length=50)
	artista = models.CharField(max_length=50)
	album =  models.CharField(max_length=50)
	reproducida = models.IntegerField()
	def __unicode__(self):
		return self.nombre



class Cancion(models.Model):
	musica = models.ForeignKey(Musica)
	votoPositivos = models.IntegerField()
	votoNegativos = models.IntegerField()
	total= models.IntegerField()
	def __unicode__(self):
		return "%s-%s" % (self.musica.nombre,self.musica.artista)
	def  votos(self):
		self.total=self.votoPositivos - self.votoNegativos
		self.save()
		return (self.votoPositivos - self.votoNegativos)


class Lista(models.Model):
	cancion =  models.ManyToManyField(Cancion)


	#que haces cuando no te gsta la musica
	#la que no me importa no es mi primer cliente

	#Yo creo que _Cliente_ tiene un proble con _problema_ que hace sentir _sentimiento_
