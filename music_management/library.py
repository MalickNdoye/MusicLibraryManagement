from music_management.artist import Artist
from music_management.music import MusicTitle
from music_management.playlist import Playlist


class MusicLibrary:

    def __init__(self):
        self.artists = {}
        self.playlists = {}
        self.uncategorized = []

    def add_song(self, msc_obj):
        if isinstance(msc_obj, MusicTitle):
            singer = msc_obj.artist
            if self.artists.get(singer, None) is not None:
                artist = self.artists[singer]
                artist.add_song(msc_obj)
            else:
                self.artists[singer] = Artist(name=singer, msc=msc_obj)
        else:
            self.uncategorized.append(msc_obj)

    @property
    def nb_artists(self):
        return len(self.artists)

    @property
    def nb_songs(self):
        nb = 0
        for artist in self.artists:
            nb += self.artists[artist].nb_songs
        return nb

    @property
    def nb_duplicates(self):
        nb = 0
        for artist in self.artists:
            nb += self.artists[artist].nb_duplicate
        return nb

    @property
    def all_songs(self):
        songs = []
        for artist in self.artists.values():
            for song in artist.get_songs():
                songs.append(song)
        return songs

    def get_duplicates(self):
        duplicates = []
        for artist in self.artists:
            for song in self.artists[artist].get_duplicates():
                duplicates.append(song)
        return duplicates

    def add_playlist(self, msc_obj):
        if isinstance(msc_obj, Playlist):
            if self.playlists.get(msc_obj.name, None) is None and msc_obj.name != '':
                self.playlists[msc_obj.name] = msc_obj
            for song in msc_obj.playlist:
                self.add_song(song)
        else:
            self.uncategorized.append(msc_obj)
