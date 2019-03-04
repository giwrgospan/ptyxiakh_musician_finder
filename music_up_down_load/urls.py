"""" Βάζουμε τα url που σχετίζονται με το music_up_down_load app(m_u_d_l) τα οποία θα κάνουμε import στο urls.py του
musician_finder . Στην 10 κάνουμε home-page την m_u_d_l και της δίνουμε από το view το index"""

from django.urls import path, re_path

# Από τον current directory(music_up_down_load) βρές το αρχείο views και κάντο import
from . import views

app_name = 'music_up_down_load'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<album_id>[0-9]+)$', views.details, name='details'),
    re_path(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
    re_path(r'^album-add$', views.AlbumCreate.as_view(), name='album-add'),

]
