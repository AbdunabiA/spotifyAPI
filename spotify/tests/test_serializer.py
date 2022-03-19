from music.serializers import ArtistSerializer, SongSerializer
from unittest import TestCase
from music.models import Artist

class TestArtistSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Moting", photo="", description="Believe")
    def test_data(self):
        data = ArtistSerializer(self.artist).data
        assert data["id"] is not None
        self.assertEqual(data["name"], "Moting")
        self.assertEqual(data["description"], "Believe")
        assert data["photo"] == ""

class TestSongSerializer(TestCase):
    def test_not_valid(self):
        song = {
            "id": 1,
            "name": "Hello",
            "cover": "",
            "lyrics": "",
            "duration": "00:03:43",
            "source": "https://www.example.com/hello.mpg4",
            "album": 1,

        }
        ser = SongSerializer(data=song)
        assert ser.is_valid() == False
        assert ser.errors['source'][0] == "Bunaqa qo'shiq formati yo'q!"

    def test_valid(self):
        song = {
            "id": 1,
            "title": "Hello",
            "cover": "",
            "lyrics": "",
            "duration": "00:03:43",
            "source": "https://www.example.com/hello.mp3",
            "album": 1,

        }
        ser = SongSerializer(data=song)
        assert ser.is_valid() == True
        malumot = ser.data
        assert malumot["title"] == "Hello"
        assert malumot["album"] == 1
        assert malumot["duration"] == "00:03:43"