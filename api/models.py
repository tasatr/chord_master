from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=1000)
    chords = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def set_chords(self, chordSequence):
        self.chords = chordSequence
        self.save()

    def __str__(self):
        return self.title
