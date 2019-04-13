from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, SongForm
from django.core.files.storage import FileSystemStorage
from .models import Profile, User


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
def profile(request , profile_id):
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
def composition_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'song_list.html', {'user': user})


@login_required
def upload_song(request ,user_id):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'upload_song.html', {'form': form})




