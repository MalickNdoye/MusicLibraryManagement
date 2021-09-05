import glob
import logging
import os

from music_management.filereader import read_songs_from_playlist
from music_management.library import MusicLibrary

cs_title = {'001.txt': 'Lost Imagination',
            '002.txt': 'Dust to Discovery',
            '003.txt': 'Remember Time',
            '004.txt': 'Beyond Dawn',
            '005.txt': 'Lucid Emotion',
            '006.txt': 'After Nothing',
            '007.txt': 'Blurred Radiance',
            '008.txt': 'default_title',
            '009.txt': 'Another Wanderer',
            '010.txt': 'Light Dreams',
            '011.txt': 'Goodbye Embrace',
            '012.txt': 'For Those Dreams',
            '013.txt': 'Locked Inside',
            '014.txt': 'Best of the Best',
            '015.txt': 'Our World Anew',
            '016.txt': 'Bring Me Those Days',
            '017.txt': 'Light the Way',
            '018.txt': 'Arcane Stars',
            '019.txt': 'Light Ripple',
            '020.txt': 'Moment Alone',
            '021.txt': 'Interstellar Escape',
            '022.txt': 'Still Beauty',
            '023.txt': 'Falling Through',
            '024.txt': 'Discover Wonder',
            '025.txt': 'Follow The Clouds',
            '026.txt': 'Anywhere From The Past',
            '027.txt': 'First We Fly',
            '028.txt': 'Hollow Embrace',
            '029.txt': 'Moonlight Passage',
            '030.txt': 'Tomorrow Farewell - Vocal Chillout Mix',
            '031.txt': 'A Night In The Stars',
            '032.txt': 'Black Dawn',
            '033.txt': 'Alone On Earth',
            '034.txt': 'Light Synergy'}


def append_title_to_file(file_name):
    path = os.path.join(os.curdir, '..', 'resources', 'Title')
    filepath = os.path.join(path, file_name)
    with open(filepath, 'a') as file:
        line = '\n\nTitle : ' + cs_title[file_name] + '\n'
        print(f'Writing "{line}" in "{filepath}"')
        file.write(line)
    print('end.')


def update_compilation_title():
    cs_dir = os.path.join('D:\\', 'Music', 'Classement par Genre', 'Ambient', 'Chillout Soundscapes', '*.mp3')
    cs_songs = glob.glob(cs_dir)
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
        cs_title[f"{song_id[i]}.txt"] = base_name[i]


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
    return directory, msc_lib