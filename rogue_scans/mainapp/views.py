from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.template import loader

from .models import Manga

# from django.views.generic import ListView
# Create your views here.

def index(request):
    mangas = Manga.objects.all()
    context = {
        'Mags' : mangas,
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def manga_details(request, id):
    manga = Manga.objects.get(id = id) 
    context = {
        'Mag' : manga,
        'current_page' : 'home'
    }
    template = loader.get_template('manga_details.html')
    return HttpResponse(template.render(context, request))


def manga(request):  # This is equivalent to ListView
    mangas = Manga.objects.all() # querying all records in the DB of entity type `Product`
    # i.e. this translates to the DQL :-> `SELECT * FROM PRODUCT;`
    # the `products` variable now contains a collection of all `Product` class objects.
    context = {
        'mags' : mangas, # the key `prods` will now be available to use in the django template design 
        'current_page' : 'mangas'

    } # context dictionary for passing data for rendering 
    template = loader.get_template('manga.html') # creating a template object from the designed template html
    return HttpResponse(template.render(context, request))