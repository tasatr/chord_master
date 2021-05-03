from rest_framework import serializers
from .models import Video, UGChords

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'video_id', 'title', 'artist', 'song', 'chords', 'created_date')

class CreateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video_id', 'title', 'artist', 'song')

class UGChordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UGChords
        fields = ('id', 'artist', 'song', 'ug_chords')
