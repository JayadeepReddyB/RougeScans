from django.urls import path
from . import views


urlpatterns =[
    path('',views.index, name = "homepage"),
    path('mangas/', views.manga, name='mangas'),
    path('mangas/<str:name>/<int:id>', views.manga_details, name = 'mag_details'),
    path('chapter/<int:chapter_id>', views.chapter_details, name='chapter_details'),
    path('mangas/search', views.searchView, name='mag_search'),
    path('mangas/add', views.AddManga.as_view(), name = 'add_manga'),
    path('chapters/add',views.AddChapter.as_view(), name = 'add_chapter'),
    path('mangas/edit/<int:pk>', views.EditManga.as_view(), name = 'edit_mag'),
    path('chapter/edit/<int:pk>', views.EditChapter.as_view(), name = 'edit_chapt'),
    path('mangas/del/<int:pk>', views.DelManga.as_view(), name = 'del_mag'),
    path('chapters/del/<int:pk>', views.DelChapter.as_view(), name = 'del_chapt'),
]
