from music_management.music import MusicTitle


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


class Playlist:

    def __init__(self, file_name):
        self.filename = file_name
        self.id = ''
        self.name = ''
        self.playlist = []

    def __str__(self):
        return self.id + str(self.playlist)

    def add_music(self, music):
        self.playlist.append(music)

    def get_playlist(self):
        return self.playlist

    @property
    def size(self):
        return len(self.playlist)

    def read_songs(self):
        try:
            self._get_name_from_file()
            with open(self.filename, encoding='utf-8') as file:
                for line in file:
                    if 'Title' not in line and len(line) > 6:
                        timestamp, song = _parse_time_stamp(line)
                        artist, title = _parse_song(song)
                        msc = MusicTitle(artist, title)
                        msc.add_playlist_presence(self.name, timestamp)
                        self.add_music(msc)
        except IOError as err:
            print(err)

    def _get_name_from_file(self):
        try:
            with open(self.filename) as file:
                for line in file:
                    if 'Title' in line and len(line) > 6:
                        self.name = line.split(' : ')[1].strip('\n')
        except IOError as err:
            print(err)
