from django.urls import path

from music.views import MusicViewSet

app_name = 'music'

urlpatterns = [
    path(
        'music/',
        MusicViewSet.as_view({'get': 'list'}),
        name='district_organizations',
    ),
]
