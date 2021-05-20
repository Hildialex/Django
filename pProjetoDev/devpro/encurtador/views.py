from django.http import HttpResponse
from django.shortcuts import render, redirect
from devpro.encurtador.models import UrlRedirect

# Create your views here.
def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destino)