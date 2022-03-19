from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import *
from .serializers import *

# class ArtistAPIViewSet(ModelViewSet):
#         serializer_class = ArtistSerializer
#         queryset = Artist.objects.all()
#
#         @action(methods=["GET"], detail=True, url_path="albums")
#         def get_album(self, request, *args, **kwargs):
#                 artist = self.get_object()
#                 albums = Album.objects.filter(artist=artist)
#                 ser = AlbumSerializer(albums, many=True)
#                 return Response(ser.data)
#
#         @action(methods=["POST"], detail=True, url_path="album")
#         def post_album(self, request, *args, **kwargs):
#                 artist = self.get_object()
#                 album = request.data
#                 album['artist'] = artist.id
#                 ser = AlbumSerializer(data=album)
#                 if ser.is_valid():
#                     ser.save()
#                 return Response(ser.data)
#
# class AlbumAPIViewSet(ModelViewSet):
#         serializer_class = AlbumSerializer
#         queryset = Album.objects.all()
#
#         @action(methods=["GET"], detail=True, url_path="songs")
#         def get_a_song(self, request, *args, **kwargs):
#                 album=self.get_object()
#                 songs=Song.objects.filter(album=album)
#                 ser = SongSerializer(songs, many=True)
#                 return Response(ser.data)
#
#         @action(methods=["POST"], detail=True, url_path="song")
#         def post_a_song(self, request, *args, **kwargs):
#                 album = self.get_object()
#                 song = request.data
#                 song['album'] = album.id
#                 ser = SongSerializer(data=song)
#                 if ser.is_valid():
#                     ser.save()
#                 return Response(ser.data)
class ArtistListAPIView(ListCreateAPIView):
        search_fields = ['name', 'photo', 'description']
        ordering_fields = ['name', 'photo', 'description']
        filter_backends = (filters.SearchFilter, filters.OrderingFilter)
        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer

class ArtistRetrieveAPIView(RetrieveUpdateDestroyAPIView):
        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer

class AlbumListAPIView(ListCreateAPIView):
        search_fields = ['name', 'cover', 'artist']
        ordering_fields = ['name', 'cover', 'artist']
        filter_backends = (filters.SearchFilter, filters.OrderingFilter)
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer

class AlbumRetrieveAPIView(RetrieveUpdateDestroyAPIView):
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer

class SongListAPIView(ListCreateAPIView):
        search_fields = ['name', 'cover', 'source', 'lyrics', 'duration', 'album']
        ordering_fields = ['name', 'cover', 'source', 'lyrics', 'duration', 'album']
        filter_backends = (filters.SearchFilter, filters.OrderingFilter)
        queryset = Song.objects.all()
        serializer_class = SongSerializer
class SongRetrieveAPIView(RetrieveUpdateDestroyAPIView):
        queryset = Song.objects.all()
        serializer_class = SongSerializer


# class SongAPIViewSet(ModelViewSet):
#         serializer_class = SongSerializer
#         queryset = Song.objects.all()
#         pagination_class = LimitOffsetPagination


