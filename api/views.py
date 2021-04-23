from django.shortcuts import render
from rest_framework import generics
from .serializers import VideoSerializer
from .models import Video

# Create your views here.
class VideoView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
