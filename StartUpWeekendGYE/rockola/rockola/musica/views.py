from django.shortcuts import render
from form import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404, render



def test1(request):
    	return render(request, 'index.html',{'salida' : 'aa'})

def selectMusica(request):
	if request.method == 'POST':
		form = selectMusicForm(request.POST)
		if not Cancion.objects.filter(musica=Musica.objects.get(nombre=request.POST['musica'])).exists():
			if (request.POST['musica'] !=u''):
				cancion = Cancion.objects.create(musica=Musica.objects.get(nombre=request.POST['musica']), votoPositivos=1,votoNegativos=0,total=1)
				cancion.save()
				return HttpResponseRedirect('.')
		return HttpResponseRedirect('/encola')
	else:
		form = selectMusicForm()
		return render(request, 'elegir.html', {'form': form})

def like(request,id1):
	cancion = get_object_or_404(Cancion,musica_id=id1)
	cancion.votoPositivos+= 1
	i=cancion.votos()
	cancion.save()
	return HttpResponseRedirect('/rank')

def disLike(request,id1):
	cancion = get_object_or_404(Cancion,musica_id=id1)
	cancion.votoNegativos+= 1
	i=cancion.votos()
	cancion.save()
	return HttpResponseRedirect('/rank')


def musicaLista(request):
	cancion = Cancion.objects.all().order_by("-total")

	return render(request, 'rank.html',{'canciones':cancion})

def server(request):
	cancion = Cancion.objects.all().order_by("-total")

	return render(request, 'index3.html',{'canciones':cancion})

def encola(request):
	return render(request, 'encola.html')
def inicio(request):
	return render(request, 'principa.html')