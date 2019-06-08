from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, SongForm, LyricsForm, BirthDForm
from django.core.files.storage import FileSystemStorage
from .models import Profile, User, Song, Lyrics
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from .filters import ProfileFilter
from django.db.models import Count


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ο λογαριασμός σας ανανεώθηκε!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u = UserUpdateForm
        p = ProfileUpdateForm

    context = {

        'u_form': u_form,
        'p_form': p_form,

     }
    return render(request, 'profile.html', context)


@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        return redirect('song_list')
    return render(request, 'upload.html', context)


@login_required
def composition_list(request):
    user = request.user
    public = SongForm()
    return render(request, 'song_list.html', {'user': user, 'public': public})


@login_required
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('song_list')
    else:
        form = SongForm()

    return render(request, 'upload_song.html', {'form': form})


@login_required
def lyrics_list(request):
    user = request.user
    return render(request, 'lyrics_list.html', {'user': user})


@login_required
def upload_lyrics(request):
    if request.method == 'POST':
        form = LyricsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('lyrics_list')
    else:
        form = LyricsForm()

    return render(request, 'upload_lyrics.html', {'form': form})


@login_required
def profile_search(request):

    profile_list = Profile.objects.all()
    profile_filter = ProfileFilter(request.GET, queryset=profile_list)
    profile_count = ProfileFilter(request.GET, queryset=profile_list).qs.count()
    submit = request.GET.get('Submit', False)

    return render(request, 'profile_list.html', {'filter': profile_filter, 'submit': submit, 'profiles': profile_count })


@login_required
def profile_appearance(request, prof_id):
    prof = get_object_or_404(Profile, pk=prof_id)
    userp = prof.user
    form = SignUpForm()
    return render(request, 'profile_appearance.html', {'profile': prof, 'form': form, 'user': userp} )


@login_required
def song_delete(request, song_id):
    song = get_object_or_404(Song, pk= song_id)
    if request.method == "POST":
        user = request.user
        song.delete()
        messages.success(request, 'Το αρχείο διαγράφηκε')
        return redirect('song_list')

    return render(request,'song_delete.html', {'song': song})


@login_required
def lyric_delete(request, lyric_id):
    lyric = get_object_or_404(Lyrics, pk= lyric_id)
    if request.method == "POST":
        user = request.user
        lyric.delete()
        messages.success(request, 'Το αρχείο διαγράφηκε')
        return redirect('lyrics_list')

    return render(request, 'lyric_delete.html', {'lyric': lyric})