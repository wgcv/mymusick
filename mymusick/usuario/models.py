from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, unique=True)
	def __str__(self):
		return self.user.username