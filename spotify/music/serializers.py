from django.core.exceptions import ValidationError

from .models import *
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name", "photo", "description"]
    def validate_name(self,qiymat):
        if len(qiymat) <= 2:
            raise ValidationError("Ism kamida 3ta xarfdan iborat bolishi shart")
        return qiymat
    def validate_photo(self,qiymat):
        oxiri = qiymat[-3:]
        if oxiri != 'png':
            raise ValidationError("Rasm png formatta boliwi wart")
        return qiymat
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "cover", "artist"]

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ["id", "name", "cover", "source", "lyrics", "duration", "album"]

    def validate_source(self, source):
        if not source.endswith('mp3'):
            raise ValidationError("Bunaqa Qoshiq formati yoq")
        return source