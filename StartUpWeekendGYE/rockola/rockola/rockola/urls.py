from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rockola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^prueba/', 'spotify.views.prueba', name='prueba'),
    url(r'^agregar/', 'musica.views.selectMusica', name='selectMusica'),
    url(r'^like/(\d+)$', 'musica.views.like', name='like'),
    url(r'^dislike/(\d+)$', 'musica.views.disLike', name='disLike'),
	url(r'^rank/', 'musica.views.musicaLista', name='musicaLista'),
   	url(r'^encola/', 'musica.views.encola', name='enola'),
   	url(r'^server/', 'musica.views.server', name='server'),
    url(r'^$', 'musica.views.inicio', name='inicio'),

    url(r'^admin/', include(admin.site.urls)),

)
