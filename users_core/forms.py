from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Song, Lyrics


YEARS = [x for x in range(1940, 2019)]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Όνομα')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Επίθετο')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Email')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label='Ημερομηνία Γένννησης')
    password1 = forms.CharField( label='Κωδικός Πρόσβασης', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Επιβεβαίωση Κωδικού Πρόσβασης', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date')
        labels = {'username': "Όνομα Χρήστη", }


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Όνομα')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Επίθετο')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {'username': "Όνομα Χρήστη", }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'music_category', 'music_nature']
        labels = {'music_category': "Μουσικά Ενδιαφέροντα", 'image': 'Εικόνα Προφίλ',
                  'music_nature': 'Μουσικές Ιδιότητες'}


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('composition_title', 'composition')


class LyricsForm(forms.ModelForm):
    class Meta:
        model = Lyrics
        fields = ('lyrics_title', 'lyrics')

