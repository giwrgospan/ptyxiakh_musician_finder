from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Song, Lyrics

# widget=forms.SelectDateWidget(years=YEARS)
YEARS = [x for x in range(1940, 2019)]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Όνομα')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Επίθετο')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Email')

    password1 = forms.CharField( label='Κωδικός Πρόσβασης', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Επιβεβαίωση Κωδικού Πρόσβασης', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
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

    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label='Ημερομηνία Γένννησης')

    class Meta:

        model = Profile
        fields = ['birth_date', 'image',  'music_nature', 'rock', 'metal', 'punk', 'pop', 'blues', 'jazz', 'funk', 'soul',
                  'electronic', 'hiphop_rap', 'greek', 'other',]
        labels = {'rock': "Rock", 'image': 'Εικόνα Προφίλ',
                  'music_nature': 'Μουσικές Ιδιότητες',}


class SongForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['composition'].required = True
        self.fields['composition_title'].required = True

    class Meta:
        model = Song
        fields = ('composition_title', 'composition','is_public' )


class LyricsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LyricsForm, self).__init__(*args, **kwargs)
        self.fields['lyrics'].required = True
        self.fields['lyrics_title'].required = True

    class Meta:
        model = Lyrics
        fields = ('lyrics_title', 'lyrics')


class BirthDForm(forms.ModelForm):

    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label='Ημερομηνία Γένννησης')

    class Meta:

        model = Profile
        fields = ['birth_date']


