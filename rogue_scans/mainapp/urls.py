from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name = "homepage"),
    path('mangas/<int:id>', views.manga_details, name = 'mag_details'),
    path('mangas/', views.manga, name='mangas'),
    path('mangas/search', views.searchView, name='mag_search')
]