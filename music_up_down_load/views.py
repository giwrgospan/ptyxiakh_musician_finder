from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music_up_down_load/index.html', {'all_albums': all_albums})


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music_up_down_load/details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music_up_down_load/details.html', {'album': album, 'error_message': "Unvalid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music_up_down_load/details.html', {'album': album})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']




