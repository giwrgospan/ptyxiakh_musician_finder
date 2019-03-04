from django.db import models
from django.urls import reverse
""" Στη 7 δηλώνουμε τι τύπου δεδομένα μπορεί να έχει το column artist(πάντα βάζουμε max_length) """
# Create your models here.  Τρόπος αποθήκευσης δεδομένων δλδ πίνακες της βάσης δεδομένων(title,artist κλπ)


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('music_up_down_load:details', kwargs={'album_id': self.pk})

    def __str__(self):
        return "%s - %s" % (self.artist, self.album_title)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title



