from music_management import logger
from music_management.music import MusicTitle
from music_management.playlist import Playlist


def _parse_time_stamp(line: str) -> (int, str):
    """
        Parse the timestamp and the song name from a string.
        For example, "31:30 Killigrew - Coming Home" will return the couple of string (1890, "Killigrew - Coming Home")
    :param line: A string matching the regex "[0-9]+:[0-9]{2} .*"
    :return: the timestamp converted to seconds and the song artist and name
    :rtype: int, str
    """
    timestamp = line[0:5]
    song = line[6:-1]
    # time = "01:34"
    timestamp = sum(x * int(t) for x, t in zip([60, 1], timestamp.split(":")))
    return timestamp, song


def _parse_song(song: str) -> (str, str):
    """
        Parse the artist name and the title of the song from a string.
        For example, "Killigrew - Coming Home" will return the couple of string ("Killigrew", "Coming Home")
    :param song: A string matching the regex ".* - .*"
    :return: The artist name and the title of the song
    :rtype: str, str
    """
    parse = song.split(' - ', 2)
    artist = parse[0]
    title = parse[1]
    return artist, title


def _get_name_from_file(filename: str) -> str:
    """
        Get the name (of the playlist) from the file.
        It searches the pattern "Title : .*" in the file and returns it.
        Otherwise, it returns "Title not found in file"
    :param filename: Path of the file
    :return:  Name of the playlist
    :rtype: str
    :exception IOError when filename or file path is wrong
    """
    try:
        with open(filename, encoding='utf-8') as file:
            for line in file:
                if 'Title' in line and len(line) > 6:
                    return line.split(' : ')[1].strip('\n')
        return 'Title not found in ' + filename
    except IOError as err:
        print(err)


def read_songs_from_playlist(filename: str, pl_id: str = '0') -> Playlist:
    """
        Read songs from file and create the correct Playlist Object
    :param filename: Path of the file
    :param pl_id: ID of the playlist
    :return: Playlist object
    :rtype: Playlist
    """
    try:
        pl_title = _get_name_from_file(filename)
        playlist = Playlist(name=pl_title, pl_id=int(pl_id))
        logger.info('Opening and reading the file : '+filename)
        with open(filename, encoding='utf-8') as file:
            for line in file:
                if 'Title' not in line and len(line) > 6:
                    timestamp, song = _parse_time_stamp(line)
                    artist, title = _parse_song(song)
                    msc = MusicTitle(artist, title)
                    msc.add_playlist_presence(pl_title, timestamp)
                    playlist.add_music(msc)
        logger.info('Closing file : ' + filename)
        return playlist
    except IOError as err:
        print(err)
