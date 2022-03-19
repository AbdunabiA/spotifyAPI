from django.contrib import admin
from django.urls import path, include
# from music.views import ArtistAPIViewSet, AlbumAPIViewSet, SongAPIViewSet
from rest_framework.routers import DefaultRouter
from music.views import ArtistListAPIView, ArtistRetrieveAPIView,AlbumListAPIView, AlbumRetrieveAPIView,SongListAPIView, SongRetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

ro = DefaultRouter()
# ro.register('artist', ArtistAPIViewSet)
# ro.register('album', AlbumAPIViewSet)
# ro.register('song', SongAPIViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(ro.urls)),
    path('artist/', ArtistListAPIView.as_view(), name = 'artist-list'),
    path('artist/<int:pk>', ArtistRetrieveAPIView.as_view(), name = 'artist-retrieve'),
    path('album/', AlbumListAPIView.as_view(), name = 'album-list'),
    path('album/<int:pk>', AlbumRetrieveAPIView.as_view(), name = 'album-retrieve'),
    path('song/', SongListAPIView.as_view(), name = 'song-list'),
    path('song/<int:pk>', SongRetrieveAPIView.as_view(), name = 'song-retrieve'),
    path('get-token', TokenObtainPairView.as_view()),
    path('refresh-token', TokenRefreshView.as_view())
]
