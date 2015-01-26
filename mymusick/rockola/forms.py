from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class Registrar(UserCreationForm):
		class Meta:
			model = User
			fields = ('username','first_name','last_name','email')