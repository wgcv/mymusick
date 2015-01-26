from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymusick.views.home', name='home'),
	url(r'^$', 'rockola.views.home', name='home'),
    url(r'^registrar/$', 'rockola.views.register', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<local>\w+)/', include('rockola.urls')),
)
