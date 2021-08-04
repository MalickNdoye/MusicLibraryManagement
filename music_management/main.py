import os.path

from music_management.library import MusicLibrary
from music_management.playlist import Playlist

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

    with open(os.path.join(directory, "all_songs.txt"), 'w', encoding='utf-8') as file:
        lines = []
        for duplicate in msc_lib.all_songs:
            # print(duplicate)
            lines.append(str(duplicate) + '\n')
        file.writelines(lines)

    with open(os.path.join(directory, "duplicated_songs.txt"), 'w', encoding='utf-8') as file:
        lines = []
        for duplicate in msc_lib.get_duplicates():
            # print(duplicate)
            line = str(duplicate) + '\n'
        file.writelines(lines)
    print('end.')
