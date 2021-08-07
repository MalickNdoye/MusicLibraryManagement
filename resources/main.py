import os.path
import logging

from music_management.filereader import read_songs_from_playlist
from music_management.filewriter import write_songs_in_file
from music_management.library import MusicLibrary

def _set_logger_settings():
    logger_main = logging.getLogger('music_management')
    logger_main.setLevel(logging.INFO)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # add the handler to the logger
    logger_main.addHandler(ch)
    return logger_main

if __name__ == '__main__':
    logger = _set_logger_settings()
    # logger.addHandler(logging.StreamHandler())
    msc_lib = MusicLibrary()
    nb_songs = 0
    directory = os.path.join(os.path.curdir, 'Title')
    for i in range(1, 35):
        path = os.path.join(directory, f"{i:03}.txt")
        playlist = read_songs_from_playlist(path, pl_id=f"{i:03}")
        nb_songs += playlist.size
        msc_lib.add_playlist(playlist)
    logger.info('number of songs loaded : ' + str(nb_songs))
    logger.info('number of artists : ' + str(msc_lib.nb_artists))
    logger.info('number of songs : ' + str(msc_lib.nb_songs))
    logger.info('number of duplicate : ' + str(msc_lib.nb_duplicates))

    write_songs_in_file(os.path.join(directory, "duplicated_songs.txt"), *msc_lib.get_duplicates())

    logger.info('end.')
