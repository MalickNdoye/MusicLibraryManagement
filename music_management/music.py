

class MusicTitle:
    """
        Class that describe a song
    :param artist: The name of the artist
    :type artist: str
    :param title: The title/name of the song
    :type title: str
    :returns: Nothing
    :rtype: none
    """

    def __init__(self, artist: str = '', title: str = '') -> None:
        """
            Initialize the object
        :param artist: The name of the artist. Default value is an empty string
        :type artist: str
        :param title: The title/name of the song. Default value is an empty string
        :type title: str
        :returns: Nothing
        :rtype: none
        """
        self.artist = artist
        self.title = title
        self.in_playlist = {}
        self.duplicated = False

    def __str__(self) -> str:
        """
            Reformat the string version of the object
        :return: string of the object
        :rtype: str
        """
        basic_format = '{:<35}| {:<36}| {}'
        pp = ""
        for pl in self.in_playlist:
            one_play = pl + '('
            for tm in self.in_playlist[pl]:
                one_play += f'{tm//60:02}:{tm%60:02}, '
            one_play = one_play[:-2] + ')'
            pp += one_play + ' - '
        pp = pp[:-3]
        return basic_format.format(self.artist, self.title, pp)
        # return self.artist + '\t|\t' + self.title + '\t| playlist presence :\t' + str(self.in_playlist)

    def add_playlist_presence(self, pl_name: str, timestamp: list) -> None:
        """
            Add the music title to a playlist and update the in_playlist dictionary
        :param pl_name: Name of the playlist
        :param timestamp: Timestamp of the song in the playlist
        :return: Nothing
        :rtype: None
        """
        if isinstance(timestamp, list):
            for tms in timestamp:
                self.add_playlist_presence(pl_name=pl_name, timestamp=tms)
        else:
            if self.in_playlist.get(pl_name, None) is not None:
                self.in_playlist[pl_name].append(timestamp)
            else:
                self.in_playlist[pl_name] = [timestamp]

    def get_playlist_presence(self) -> dict:
        """
            Return the in_playlist dictionary
        :return: Dictionary of Playlist Object
        :rtype: dict
        """
        return self.in_playlist

    def csv_str(self) -> str:
        """
            Reformat the string version of the object in a CSV format
        :return: string of the object
        :rtype: str
        """
        csv_line = ''
        for playlist in self.in_playlist:
            for time in self.in_playlist[playlist]:
              csv_line += self.artist + ';' + self.title + ';' + playlist + ';' + f'{time//60:02}:{time%60:02}' + ';\n'
        return csv_line