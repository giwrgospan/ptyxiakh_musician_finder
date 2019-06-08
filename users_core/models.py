from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from multiselectfield import MultiSelectField
from django.conf import settings
import django_filters
from django import forms
from django.core.validators import FileExtensionValidator


YEARS = [x for x in range(1940, 2019)]


class Profile(models.Model):
    ROCK_CHOICES = (
        ('Classic Rock', 'Classic Rock'),
        ('Progressive Rock', 'Progressive Rock'),
        ('Post Rock', 'Post Rock'),
        ('Rock&Roll', 'Rock&Roll'),
        ('Psychedelic Rock', 'Psychedelic Rock'),
        ('Hard Rock', 'Hard Rock'),
        ('Garage Rock', 'Garage Rock'),
        ('Surf Rock', 'Surf Rock'),
        ('Rockabilly', 'Rockabilly'),
    )
    METAL_CHOICES = (
        ('Black Metal', 'Black Metal'),
        ('Death Metal', 'Death Metal'),
        ('Thrash Metal', 'Thrash Metal'),
        ('Doom Metal', 'Doom Metal'),
        ('Progressive Metal', 'Progressive Metal'),
        ('Sludge Metal', 'Sludge Metal'),
        ('Heavy Metal', 'Heavy Metal'),
        ('Metalcore', 'Metalcore'),
        ('Grindcore', 'Grindcore'),
    )
    PUNK_CHOICES = (
        ('Punk Rock', 'Punk Rock'),
        ('Pop Punk', 'Pop Punk'),
        ('Garage Punk', 'Garage Punk'),
        ('Hardcore Punk', 'Hardcore Punk'),
        ('Thrash Punk', 'Thrash Punk'),
        ('Crust Punk', 'Crust Punk'),
        ('Folk Punk', 'Folk Punk'),
        ('Ska Punk', 'Ska Punk'),
    )
    POP_CHOICES = (
        ('Indie Pop', 'Indie Pop'),
        ('Synth Pop', 'Synth Pop'),
        ('Power Pop', 'Power Pop'),
        ('Dream Pop', 'Dream Pop'),
        ('Noise Pop', 'Noise Pop'),
        ('Experimental Pop', 'Experimental Pop'),
        ('Jangle Pop', 'Jangle Pop'),
    )
    BLUES_CHOICES = (
        ('Blues', 'Blues'),
        ('Blues Rock', 'Blues Rock'),
        ('Country Blues', 'Country Blues'),
        ('Rythm & Blues', 'Rythm & Blues'),
        ('Electric Blues', 'Electric Blues'),
        ('Boogie-Woogie', 'Boogie-Woogie'),
        ('Bluegrass', 'Bluegrass'),
        ('Delta Blues', 'Delta Blues'),
    )
    JAZZ_CHOICES = (
        ('Jazz', 'Jazz'),
        ('Nu Jazz', 'Nu Jazz'),
        ('Modern Jazz', 'Modern Jazz'),
        ('Free Jazz', 'Free Jazz'),
        ('Soul Jazz', 'Soul Jazz'),
        ('Swing', 'Swing'),
        ('Latin Jazz', 'Latin Jazz'),
        ('Vocal Jazz', 'Vocal Jazz'),
        ('Spiritual Jazz', 'Spiritual Jazz'),
    )
    FUNK_CHOICES = (
        ('Funk', 'Funk'),
        ('Funk Jam', 'Funk Jam'),
        ('Deep Funk', 'Deep Funk'),
        ('Funk Rock', 'Funk Rock'),
        ('Jazz Funk', 'Jazz Funk'),
        ('g-Funk', 'g-Funk'),
        ('Electro Funk', 'Electro Funk'),
        ('Go-go', 'Go-go'),
    )
    SOUL_CHOICES = (
        ('Soul', 'Soul'),
        ('Neo-Soul', 'Neo-Soul'),
        ('Gospel', 'Gospel'),
    )
    ELECTRONIC_CHOICES = (
        ('House', 'House'),
        ('Electronica', 'Electronica'),
        ('Downtempo', 'Downtempo'),
        ('Techno', 'Techno'),
        ('Electro', 'Electro'),
        ('Dubstep', 'Dubstep'),
        ('Drum % Bass', 'Drum % Bass'),
        ('Trance', 'Trance'),
        ('Dub', 'Dub'),
        ('Vaporwave', 'Vaporwave'),
    )

    HIP_HOP_RAP_CHOICES = (
        ('Rap', 'Rap'),
        ('Trap', 'Trap'),
        ('Instrumental Hip-Hop', 'Instrumental Hip-Hop'),
        ('Boom-Bap', 'Boom-Bap'),
        ('Beat-tape', 'Beat-tape'),
    )
    GREEK_CHOICES = (
        ('Έντεχνο', 'Έντεχνο'),
        ('Λαϊκό', 'Λαϊκό'),
        ('Ρεμπέτεκο', 'Ρεμπέτεκο'),
    )

    OTHER_CHOICES = (
        ('Ska', 'Ska'),
        ('No Wave', 'No Wave'),
        ('Folk', 'Folk'),
        ('New wave', 'New wave'),
        ('Swing', 'Swing'),
        ('Gospel', 'Gospel'),
    )

    MUSIC_NATURE = (
        ('Drummer', 'Drummer'),
        ('Τραγουδιστής', 'Τραγουδιστής'),
        ('Κιθαρίστας', 'Κιθαρίστας'),
        ('Μπασίστας', 'Μπασίστας'),
        ('Στιχουργός', 'Στιχουργός '),
        ('Σαξοφωνίστας', 'Σαξοφωνίστας '),
        ('Κλαριτζής', 'Κλαριτζής '),
        ('Dj', 'Dj '),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    rock = MultiSelectField(choices=ROCK_CHOICES, blank=True)
    metal = MultiSelectField(choices=METAL_CHOICES, blank=True)
    punk = MultiSelectField(choices=PUNK_CHOICES, blank=True)
    pop = MultiSelectField(choices=POP_CHOICES, blank=True)
    blues = MultiSelectField(choices=BLUES_CHOICES, blank=True)
    jazz = MultiSelectField(choices=JAZZ_CHOICES, blank=True)
    funk = MultiSelectField(choices=FUNK_CHOICES, blank=True)
    soul = MultiSelectField(choices=SOUL_CHOICES, blank=True)
    electronic = MultiSelectField(choices=ELECTRONIC_CHOICES, blank=True)
    hiphop_rap = MultiSelectField(choices=HIP_HOP_RAP_CHOICES, blank=True)
    greek = MultiSelectField(choices=GREEK_CHOICES, blank=True)
    other = MultiSelectField(choices=OTHER_CHOICES, blank=True)
    music_nature = MultiSelectField(choices=MUSIC_NATURE, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Song(models.Model):
    composition_title = models.CharField(max_length=100, blank=True)
    composition = models.FileField(upload_to='uploaded_music', max_length=100, blank=True,
                                   validators=[FileExtensionValidator(allowed_extensions=['mp3', 'flac', 'wav'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.composition_title} composition'


class Lyrics(models.Model):
    lyrics_title = models.CharField(max_length=100, blank=True)
    lyrics = models.FileField(upload_to='uploaded_lyrics', max_length=100, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.lyrics_title} lyrics'








