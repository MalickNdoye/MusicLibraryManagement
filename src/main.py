import os.path

from src.library import MusicLibrary
from src.playlist import Playlist

if __name__ == '__main__':
    msc_lib = MusicLibrary()
    nb_songs = 0
    directory = os.path.join(os.path.curdir, '../resources/Title')
    for i in range(1, 35):
        path = os.path.join(directory, f"{i:03}.txt")
        playlist = Playlist(path)
        playlist.read_songs()
        nb_songs += playlist.size
        msc_lib.add_playlist(playlist)
    print('number of songs loaded : ' + str(nb_songs))
    print('number of artists : ' + str(msc_lib.nb_artists))
    print('number of songs : ' + str(msc_lib.nb_songs))
    print('number of duplicate : ' + str(msc_lib.nb_duplicates))
    for duplicate in msc_lib.all_songs:
        print(duplicate)
    print('end.')
