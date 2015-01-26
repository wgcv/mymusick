from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from rockola.forms import *
from usuario.models import Usuario
from django.contrib.auth.models import User

# Create your views here.


def current_datetime(request,local):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % local
    return HttpResponse(html)

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def register(request):
    if request.method == 'POST':
        uf = Registrar(request.POST)
        if uf.is_valid():
            uf.save()
            useradd = User.objects.get(username=uf.cleaned_data['username'])
            usuario = Usuario(user=useradd)
            usuario.save();
            return HttpResponseRedirect('/')
    else:
        uf = Registrar()
    return render(request, 'rockola/template/register.html', dict(userform=uf))