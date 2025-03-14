from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name = "homepage"),
    path('mangas/<int:id>', views.manga_details, name = 'mag_details'),
    path('mangas/', views.manga, name='mangas'),
    path('mangas/search', views.searchView, name='mag_search'),
    path('mangas/add', views.AddManga.as_view(), name = 'add_manga'),
    path('chapters/add',views.AddChapter.as_view(), name = 'add_chapter'),
    

]