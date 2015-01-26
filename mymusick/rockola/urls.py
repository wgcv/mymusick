from django.conf.urls import url
from django.contrib import admin
from rockola import views

urlpatterns = (
    # Examples:
    # url(r'^$', 'mymusick.views.home', name='home'),
    url(r'^$', 'rockola.views.current_datetime', name='home'),

    )