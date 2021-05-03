from django.urls import path
from .views import VideoView, CreateVideoView, UGChordView
from .views import upload_chords

urlpatterns = [
    path('', VideoView.as_view()),
    path("create-video", CreateVideoView.as_view()),
    path("list-videos", VideoView.as_view()),
    path("upload-chords", upload_chords, name="upload_chords"),
    path("list-ug-chords", UGChordView.as_view())
]
