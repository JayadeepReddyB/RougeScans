from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.urls import reverse_lazy, reverse

from django.template import loader

from .models import Manga,Chapter

from django.views.generic import CreateView,UpdateView,DeleteView

# from django.views.generic import ListView
# Create your views here.

def index(request):
    mangas = Manga.objects.all()
    # I want to create a chapter view specific for the manga to shown in the index page 
    # So, How to create a view for that??
    # chapters = Chapter.objects.filter(manga=manga.id).order_by('-chapter_number')


    context = {
        'Mags' : mangas,
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def manga_details(request, id):
    manga = Manga.objects.get(id = id) 
    chapters = Chapter.objects.filter(manga=manga).order_by('-chapter_number')
    context = {
        'Mag' : manga,
        'chapts' : chapters,
        'current_page' : 'details'
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

def searchView(request):
    query = request.GET.get('search_text') # fetch the query text from GET request
    results = Manga.objects.filter(name__icontains = query) # collect the product object matching the name
    context = {
        'items' : results,
        'query' : query
    }
    template = loader.get_template('searchResults.html')
    return HttpResponse(template.render(context, request))

# 1. C - Create
class AddManga(CreateView):
    model = Manga # specifying the schema to insert record into
    fields = '__all__'
    template_name = 'addManga.html'
    success_url = reverse_lazy('mangas') # redirect to products page after adding product

class AddChapter(CreateView):
    model = Chapter
    fields = '__all__'
    template_name = 'addChapter.html'
    def get_success_url(self):
        return reverse('mag_details', kwargs={'id' : self.object.manga.id})

class EditManga(UpdateView):
    model = Manga
    fields = "__all__"
    template_name = 'editManga.html'
    # success_url = reverse_lazy('mag_details Mag.id') # The reverse_lazy the id format is not proper 
    def get_success_url(self):
        return reverse('mag_details', kwargs={'id' : self.object.pk})
class EditChapter(UpdateView):
    model = Chapter
    fields = ["title", "chapter_number", "release_date"]
    template_name = "editChapter.html"
    def get_success_url(self):
        return reverse('mag_details', kwargs={'id' : self.object.manga.id})
    
class DelManga(DeleteView):
    model = Manga
    template_name = 'delManga.html'
    success_url = reverse_lazy('mangas')

class DelChapter(DeleteView):
    model = Chapter
    template_name = 'delChapter.html'
    def get_success_url(self):
        return reverse('mag_details', kwargs={'id' : self.object.manga.id})

