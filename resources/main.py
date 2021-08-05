import os.path

from music_management.filereader import read_songs_from_playlist
from music_management.filewriter import write_songs_in_file
from music_management.library import MusicLibrary


if __name__ == '__main__':
    msc_lib = MusicLibrary()
    nb_songs = 0
    directory = os.path.join(os.path.curdir, 'Title')
    for i in range(1, 35):
        path = os.path.join(directory, f"{i:03}.txt")
        playlist = read_songs_from_playlist(path)
        nb_songs += playlist.size
        msc_lib.add_playlist(playlist)
    print('number of songs loaded : ' + str(nb_songs))
    print('number of artists : ' + str(msc_lib.nb_artists))
    print('number of songs : ' + str(msc_lib.nb_songs))
    print('number of duplicate : ' + str(msc_lib.nb_duplicates))

    write_songs_in_file(os.path.join(directory, "duplicated_songs.txt"), *msc_lib.get_duplicates())

    print('end.')
