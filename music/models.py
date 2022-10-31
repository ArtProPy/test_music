from django.db import models


class Executor(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'music'
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Album(models.Model):
    executor = models.ForeignKey(
        Executor,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='albums'
    )
    date_creation = models.IntegerField('Дата создания')

    def __str__(self):
        return f'{self.executor.name} {self.date_creation}'

    class Meta:
        app_label = 'music'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Song(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'music'
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class SongAlbum(models.Model):
    song = models.ForeignKey(Song, verbose_name='Песня', on_delete=models.CASCADE, related_name='albums')
    album = models.ForeignKey(Album, verbose_name='Альбом', on_delete=models.CASCADE, related_name='songs')
    number_in_album = models.IntegerField('Номер песни', default=1)

    def __str__(self):
        return f'{self.album} {self.song}'

    class Meta:
        app_label = 'music'
        verbose_name = 'Альбом-песня'
        verbose_name_plural = 'Альбом-песни'
