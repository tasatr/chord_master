from django.shortcuts import render
from rest_framework import generics, status
from .serializers import VideoSerializer, CreateVideoSerializer
from .models import Video
from rest_framework.views import APIView
from rest_framework.response import Response
import logging

# Create your views here.

logger = logging.getLogger("Views")

class VideoView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CreateVideoView(APIView):
    logger.error('Goodbye, cruel world!')
    serializer_class = CreateVideoSerializer

    def post(self, request, format=None):
        logger.error('#####Inside post, request data: ')
        logger.error(request.data)

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        logger.error('past serializer ')
        logger.error(serializer)

        queryset = Video.objects.filter(video_id = serializer.initial_data.get('video_id'))
        if queryset.exists():
            return Response({'Already exists'}, status=status.HTTP_200_OK)

        if serializer.is_valid():
            logger.error('serializer is valid')
            video_id = serializer.data.get('video_id')
            logger.error('video_id is ')
            logger.error(video_id)
            title = serializer.data.get('title')

            queryset = Video.objects.filter(video_id = video_id)
            if queryset.exists():
                return Response({'Already exists'}, status=status.HTTP_200_OK)
            else:
                video = Video(video_id = video_id, title = title)
                video.save()
                return Response(VideoSerializer(video).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
