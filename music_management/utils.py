import glob
import logging
import os

from music_management.filereader import read_songs_from_playlist
from music_management.library import MusicLibrary
from music_management import CS_DIR, CS_TITLES, MAIN_DIR


def append_title_to_file(file_name):
    path = os.path.join(os.curdir, '..', 'resources', 'Title')
    filepath = os.path.join(path, file_name)
    with open(filepath, 'a') as file:
        line = '\n\nTitle : ' + CS_TITLES[file_name] + '\n'
        print(f'Writing "{line}" in "{filepath}"')
        file.write(line)
    print('end.')


def update_compilation_title():
    cs_songs = glob.glob(CS_DIR)
    base_name = []
    song_id = []
    for path in cs_songs:
        filename = os.path.basename(path).split('.')
        name = filename[0].replace('__', '_')
        playlist_id = filename[0].split('_', 2)[0]
        base_name.append(name[4:].replace('_', ' '))
        song_id.append(playlist_id)
    assert len(base_name) == len(song_id)
    for i in range(len(song_id)):
        CS_TITLES[f"{song_id[i]}.txt"] = base_name[i]


def set_logger_settings():
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


def main():
    logger = logging.getLogger('music_management')
    # logger.addHandler(logging.StreamHandler())
    msc_lib = MusicLibrary()
    nb_songs = 0
    directory = os.path.join(MAIN_DIR, 'Title')
    for i in range(1, 35):
        path = os.path.join(directory, f"{i:03}.txt")
        playlist = read_songs_from_playlist(path, pl_id=f"{i:03}")
        nb_songs += playlist.size
        msc_lib.add_playlist(playlist)
    logger.info('number of songs loaded : ' + str(nb_songs))
    logger.info('number of artists : ' + str(msc_lib.nb_artists))
    logger.info('number of songs : ' + str(msc_lib.nb_songs))
    logger.info('number of duplicate : ' + str(msc_lib.nb_duplicates))
    return directory, msc_lib