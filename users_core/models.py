from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from multiselectfield import MultiSelectField
from django.conf import settings


class Profile(models.Model):
    MUSIC_CHOICES = (
        ('Rock', 'Rock'),
        ('Punk', 'Punk'),
        ('Pop', 'Pop'),
        ('Hip-Hop', 'Hip-Hop'),
    )
    MUSIC_NATURE = (
        ('Drummer', 'Drummer'),
        ('Τραγουδιστής', 'Τραγουδιστής'),
        ('Κιθαρίστας', 'Κιθαρίστας'),
        ('Μπασίστας', 'Μπασίστας'),
        ('Στιχουργός', 'Στιχουργός'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    music_category = MultiSelectField(choices=MUSIC_CHOICES, blank=True)
    music_nature = MultiSelectField(choices=MUSIC_NATURE, blank=True)

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
    composition = models.FileField(upload_to='uploaded_music', max_length=100, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.composition_title} composition'







