from music_management.music import MusicTitle


class Playlist:
    """
        Class that describe a playlist
    :param pl_id: ID of the playlist. Default value is 0
    :type pl_id: int
    :param name: Name of the playlist
    :type name: str
    """

    def __init__(self, pl_id: int = 0, name: str = '') -> None:
        """
            Initialize the object
        :param pl_id: ID of the playlist. Default value is 0
        :type pl_id: int
        :param name: Name of the playlist
        :type name: str
        """
        self.id = pl_id
        self.name = name
        self.playlist = []

    def __str__(self) -> str:
        """
            Reformat the string version of the object
        :return: string of the object
        :rtype: str
        """
        return str(self.id) + str(self.playlist)

    def add_music(self, music: MusicTitle) -> None:
        """
            Add a song to the playlist
        :param music: Song to be added
        :type music: MusicTitle
        :return: Nothing
        :rtype: None
        """
        self.playlist.append(music)

    def get_playlist(self) -> list:
        """
            Return the list of song of playlist as a list of MusicTile objects
        :return: List of MusicTitle songs
        :rtype: list
        """
        return self.playlist

    @property
    def size(self) -> int:
        """
            Return the number of songs of the playlist
        :return: Number of songs of the playlist
        :rtype: int
        """
        return len(self.playlist)

