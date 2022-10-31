from rest_framework import serializers

from music.models import *


class ExecutorSerializer(serializers.ModelSerializer):
    albums = serializers.SerializerMethodField()

    @staticmethod
    def get_albums(obj):
        return [AlbumSerializer(album).data for album in obj.albums.all()]

    class Meta:
        model = Executor
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    def validate(self, attrs):
        attrs = super(SongAlbumSerializer, self).validate(attrs)
        if attrs['date_creation'] > 2022:
            raise serializers.ValidationError(f'Указана не верная дата создания: {attrs["date_creation"]}')
        return attrs

    @staticmethod
    def get_songs(obj):
        return [SongAlbumSerializer(song).data for song in obj.songs.all()]

    class Meta:
        model = Album
        fields = '__all__'


class SongAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongAlbum
        fields = '__all__'

    def validate(self, attrs):
        attrs = super(SongAlbumSerializer, self).validate(attrs)
        number = attrs.get('number_in_album', None)
        if number is None:
            raise serializers.ValidationError('Не указан номер песни')
        elif number <= 0:
            raise serializers.ValidationError(f'Номер песни указан не верно: {number}')
        elif SongAlbum.objects.filter(number_in_album=number, song=attrs['song']):
            raise serializers.ValidationError(
                f'Номер для данной песни указан для другой группы: {number}'
                f'Введите другой номер'
            )
        return attrs

