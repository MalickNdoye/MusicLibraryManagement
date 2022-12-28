from music_management import logger
from music_management.artist import Artist
from music_management.music import MusicTitle
from music_management.playlist import Playlist


class MusicLibrary:
    """
        Class of Music Library that classify all the artists and playlist of the library
    """

    def __init__(self):
        """
            Initialize the object
        """
        self.artists = {}
        self.playlists = {}
        self.uncategorized = []

    def add_song(self, msc_obj: MusicTitle) -> None:
        """
            Add a song to an artist
        :param msc_obj: MusicTilte object
        :return: Nothing
        :rtype: None
        """
        if isinstance(msc_obj, MusicTitle):
            singer = msc_obj.artist
            if self.artists.get(singer, None) is not None:
                artist = self.artists[singer]
                artist.add_song(msc_obj)
            else:
                self.artists[singer] = Artist(name=singer, msc=msc_obj)
        else:
            self.uncategorized.append(msc_obj)
            logger.error('Unknown object : ' + str(msc_obj))

    @property
    def nb_artists(self) -> int:
        """
            Return the number of artists of the library.
        :return: number of artist
        :rtype: int
        """
        return len(self.artists)

    @property
    def nb_songs(self) -> int:
        """
            Return the number of songs of the library.
        :return: number of songs
        :rtype: int
        """
        nb = 0
        for artist in self.artists:
            nb += self.artists[artist].nb_songs
        return nb

    @property
    def nb_duplicates(self) -> int:
        """
            Return the number of duplicated songs of the library.
        :return: number of duplicated titles
        :rtype: int
        """
        nb = 0
        for artist in self.artists:
            nb += self.artists[artist].nb_duplicate
        return nb

    @property
    def all_songs(self) -> list:
        """
            Return the list of al the songs of the library.
        :return: number of songs
        :rtype: list
        """
        songs = []
        for artist in self.artists.values():
            for song in artist.get_songs():
                songs.append(song)
        return songs

    def get_duplicates(self) -> list:
        """
            Return the list of duplicated songs of the library.
        :return: list of duplicated titles
        :rtype: list
        """
        duplicates = []
        for artist in self.artists:
            for song in self.artists[artist].get_duplicates():
                duplicates.append(song)
        return duplicates

    def add_playlist(self, msc_obj) -> None:
        """
            Add a playlist to the library
        :param msc_obj: Playlist object
        :return: Nothing
        :rtype: None
        """
        if isinstance(msc_obj, Playlist):
            if self.playlists.get(msc_obj.name, None) is None and msc_obj.name != '':
                self.playlists[msc_obj.name] = msc_obj
            for song in msc_obj.playlist:
                self.add_song(song)
        else:
            self.uncategorized.append(msc_obj)
            logger.error('Unknown object : ' + str(msc_obj))
