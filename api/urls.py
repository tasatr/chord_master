from django.urls import path
from .views import VideoView, CreateVideoView

urlpatterns = [
    path('', VideoView.as_view()),
    path("create-video", CreateVideoView.as_view()),
    path("list-videos", VideoView.as_view())
]
