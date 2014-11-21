from django.shortcuts import render
import spotipy
import sys
import spotipy.util as util
import sys,os
# Create your views here.
def prueba(request):
	os.environ["SPOTIPY_CLIENT_ID"]='d0f3367890dc4cb7bb3f947a240a9681'
	os.environ["SPOTIPY_CLIENT_SECRET"]='9b3df21720204637a6f60cb1ddef8d7f'
	os.environ["SPOTIPY_REDIRECT_URI"]='http://localhost/callback'
	spotify = spotipy.Spotify()
	name = 'radiohead'
	results = spotify.search(q='artist:' + name, type='artist')
    	return render(request, 'index.html',{'salida' : results})