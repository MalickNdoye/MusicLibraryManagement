from music_management import logger
from music_management.music import MusicTitle


def write_songs_in_file(filepath: str, *songs: MusicTitle) -> None:
    """
        Write a list of the songs in a file in text format
    :param filepath: Path of the file
    :param songs: List of MusicTitle objects
    :rtype: list
    :return: Nothing
    :rtype: None
    """
    logger.info('Opening and writing into file : ' + filepath)
    with open(filepath, 'w', encoding='utf-8') as file:
        lines = []
        for song in songs:
            lines.append(str(song) + '\n')
        file.writelines(lines)
    logger.info('Closing file : ' + filepath)


def write_songs_in_csv_file(filepath: str, *songs: MusicTitle) -> None:
    """
            Write a list of the songs in a file in csv  format
        :param filepath: Path of the file
        :param songs: List of MusicTitle objects
        :rtype: list
        :return: Nothing
        :rtype: None
        """
    logger.info('Opening and writing into file : ' + filepath)
    with open(filepath, 'w', encoding='utf-8') as file:
        lines = ['Artist;Title;Playlist;Timestamp;\n']
        for song in songs:
            lines.append(song.csv_str())
        file.writelines(lines)
    logger.info('Closing file : ' + filepath)