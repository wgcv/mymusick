from django import forms
from models import *
from django.forms.extras.widgets import SelectDateWidget
class selectMusicForm(forms.Form):
	musica = forms.ModelChoiceField(queryset=Musica.objects.all().values_list(('nombre'), flat=True))

	#fechaIngresoCompania = forms.DateField(widget=SelectDateWidget(years = Musica.objects.all().order_by('nombre')))
	class Meta:
		model = Cancion
		exclude = ('votoPositivos','votoNegativos',)