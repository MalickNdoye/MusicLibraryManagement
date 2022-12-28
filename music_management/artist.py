from music_management import logger
from music_management.music import MusicTitle
from hashlib import sha256

class Artist:
    """Class that describe an artist.

    :param name: The name of the artist
    :type name: str
    :param msc: The music that is linked to the artist
        (default is default MusicTitle Object)
    :type msc: MusicTitle
    :returns: Nothing
    :rtype: none
    """

    def __init__(self, name: str = '', msc: MusicTitle = MusicTitle(artist='')) -> None:
        self.artist_hash = sha256(name.lower().strip(' ')).hexdigest()
        self.name = name
        self.titles = {msc.title: msc}
        logger.info('Creating %s as Artist with the associated hash %s.',  self.name, self.artist_hash)

    def add_song(self, msc_obj: MusicTitle) -> None:
        """
            Add a song to the artist's music library
        :param msc_obj: Song associated to the artist.
        :return: None
        """
        if isinstance(msc_obj, MusicTitle):
            if self.titles.get(msc_obj.title, None) is None:
                self.titles[msc_obj.title] = msc_obj
                logger.info('Adding the song (%s) to %s catalog', msc_obj.title, self.name)
            else:
                self.titles[msc_obj.title].duplicated = True
                for pl_name in msc_obj.get_playlist_presence():
                    self.titles[msc_obj.title].add_playlist_presence(pl_name=pl_name,
                                                                     timestamp=msc_obj.in_playlist[pl_name])

    def get_duplicates(self) -> list:
        """
            Get the duplicated titles found in the title dictionary. This should return an empty list.
        :return: List of duplicated titles
        :rtype: list
        """
        duplicates = []
        for title in self.titles:
            if self.titles[title].duplicated is True:
                duplicates.append(self.titles[title])
        return duplicates

    def get_songs(self) -> list:
        """
            Return the list of titles of the artist
        :return: List of titles
        :rtype: list
        """
        return list(self.titles.values())

    @property
    def nb_songs(self) -> int:
        """
            Return the number of titles of the artist.
        :return: number of titles
        :rtype: int
        """
        return len(self.titles)

    @property
    def nb_duplicate(self) -> int:
        """
            Return the number of duplicated titles of the artist.
        :return: number of duplicated titles
        :rtype: int
        """
        nb = 0
        for msc in self.titles.values():
            if msc.duplicated is True:
                nb += 1
        return nb
