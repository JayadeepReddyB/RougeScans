from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.template import loader

from .models import Manga


# Create your views here.

def index(request):
    mangas = Manga.objects.all()
    context = {
        'Mag' : mangas
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))