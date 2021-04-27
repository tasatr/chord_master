from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'video_id', 'title', 'chords', 'created_date')

class CreateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video_id', 'title')
