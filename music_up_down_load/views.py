from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from .models import Album, Song, User1
from django.views.generic import View
from .forms import User1Form


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


def users1(request):
    all_users1 = User1.users.all()
    return render(request, 'music_up_down_load/home.html', {'all_users1': all_users1})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class User1FormView(View):
    form_class = User1Form
    template_name = 'music_up_down_load/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)  # information user posts in our form

        if form.is_valid():

            user = form.save(commit=False)  # save information locally(not in db yet)

            # clean(normalized data) (like date model)

            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            name = form.cleaned_data['Name']
            surname = form.cleaned_data['Surname']
            email = form.cleaned_data['Email']
            user.save()  # save information in db

            # return user objects if auth is ok

            user = authenticate(username=username, password=password)

            return redirect('home')

        return render(request, self.template_name, {'form': form})  # not valid user . Try again
