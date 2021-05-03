from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=1000, default='artist')
    song = models.CharField(max_length=1000, default='song')
    chords = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def set_chords(self, chordSequence):
        self.chords = chordSequence
        self.save()

    def __str__(self):
        return self.title

class UGChords(models.Model):
    artist = models.CharField(max_length=1000)
    song = models.CharField(max_length=1000)
    ug_chords = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
