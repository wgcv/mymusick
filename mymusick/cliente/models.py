from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, unique=True)
	nombre = models.CharField("Nombre del cliente", max_length=50, unique=True)
	identificacion = models.CharField("Identificacion del cliente", max_length=15, unique=True)
	mail = models.EmailField("Correo electronico", unique=True)
	fechaIngreso = models.DateField("Fecha de ingreso",auto_now=True)
	telefono = models.CharField("Telefono del cliente", max_length=15)
	def __str__(self):
		return self.nombre
class TipoLocal(models.Model):
	tipo = models.CharField("Tipo de local", max_length=50, unique=True)
	def __str__(self):
		return self.tipo

class Local(models.Model):
	id = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Cliente, unique=False)
	user = models.ForeignKey(User, unique=True)
	nombre = models.CharField("Nombre del Local", max_length=50, unique=True)
	mail = models.EmailField("Correo electronico", unique=True)
	telefono = models.CharField("Telefono del cliente", blank=True, max_length=15)
	fechaIngreso = models.DateField("Fecha de ingresoo",auto_now=True)
	fechaCorte = models.DateField("Fecha de corte",auto_now=True)
	mesesServicio = models.IntegerField("Meses de servicio",default=0)
	activo = models.BooleanField(default=True)
	interaccionesMes = models.IntegerField("Interaccion del mes",default=0)
	interaccionesTotal = models.IntegerField("Interacciones Totales",default=0)
	volumen = models.PositiveSmallIntegerField("Volumen del local",default=7)
	TipoLocal = models.ForeignKey(TipoLocal,unique=False)
	altitud = models.DecimalField("Altitu del gps", max_digits=8, decimal_places=6,null=True, blank=True)
	latitud = models.DecimalField("Latitud del gps", max_digits=8, decimal_places=6,null=True , blank=True)
	horaDj = models.TimeField()
	def __str__(self):
		return self.nombre


class DjUsuario(models.Model):
	local = models.ForeignKey(Local, unique=True)
	Usuario = models.ForeignKey(User,unique=False)




