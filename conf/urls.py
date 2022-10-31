"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

from music.views import MusicViewSet, AlbumViewSet, SongViewSet, SongAlbumViewSet

router = routers.SimpleRouter()
router.register(r'music', MusicViewSet, basename='music')
router.register(r'album', AlbumViewSet, basename='album')
router.register(r'song', SongViewSet, basename='song')
router.register(r'song-album', SongAlbumViewSet, basename='song-album')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'music'), namespace='music')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view
    from rest_framework import permissions, routers

    schema_view = get_schema_view(
        openapi.Info(
            title="Notification center API",
            default_version='0.1.0',
            description="Документация API",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns.extend(
        [
            re_path(
                r'^doc(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0),
                name='schema-json',
            ),
            path(
                'doc/',
                schema_view.with_ui('swagger', cache_timeout=0),
                name='schema-swagger-ui',
            ),
            path(
                'redoc/',
                schema_view.with_ui('redoc', cache_timeout=0),
                name='schema-redoc',
            ),
        ]
    )

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
