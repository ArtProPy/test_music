from rest_framework.viewsets import ModelViewSet

from music.models import Executor, Album, Song, SongAlbum
from music.serializers import ExecutorSerializer, AlbumSerializer, SongSerializer, SongAlbumSerializer


class MusicViewSet(ModelViewSet):
    serializer_class = ExecutorSerializer
    queryset = Executor.objects.all()
    filterset_fields = '__all__'


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    filterset_fields = '__all__'


class SongViewSet(ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    filterset_fields = '__all__'


class SongAlbumViewSet(ModelViewSet):
    serializer_class = SongAlbumSerializer
    queryset = SongAlbum.objects.all()
    filterset_fields = '__all__'
