from music_management.music import MusicTitle
from music_management.playlist import Playlist


def _parse_time_stamp(line):
    timestamp = line[0:5]
    song = line[6:-1]
    # time = "01:34"
    timestamp = sum(x * int(t) for x, t in zip([60, 1], timestamp.split(":")))
    return timestamp, song


def _parse_song(song):
    parse = song.split(' - ', 2)
    artist = parse[0]
    title = parse[1]
    return artist, title


def _get_name_from_file(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            for line in file:
                if 'Title' in line and len(line) > 6:
                    return line.split(' : ')[1].strip('\n')
        return 'Title not found in '+ filename
    except IOError as err:
        print(err)


def read_songs_from_playlist(filename, pl_id='0'):
    try:
        pl_title = _get_name_from_file(filename)
        playlist = Playlist(name=pl_title, pl_id=pl_id)
        with open(filename, encoding='utf-8') as file:
            for line in file:
                if 'Title' not in line and len(line) > 6:
                    timestamp, song = _parse_time_stamp(line)
                    artist, title = _parse_song(song)
                    msc = MusicTitle(artist, title)
                    msc.add_playlist_presence(pl_title, timestamp)
                    playlist.add_music(msc)
        return playlist
    except IOError as err:
        print(err)


