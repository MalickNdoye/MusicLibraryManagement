

class MusicTitle:

    def __init__(self, artist='', timestamp='', title=''):
        self.timestamp = timestamp
        self.artist = artist
        self.title = title
        self.in_playlist = []
        self.duplicated = False

    def __str__(self):
        return self.timestamp + '\t| ' + self.artist + '\t|\t' + self.title +\
               '\t| playlist presence :\t' + str(self.in_playlist)

    def add_playlist_presence(self, *pl_name):
        for name in pl_name:
            self.in_playlist.append(str(name).strip('\n'))

    def get_playlist_presence(self):
        return self.in_playlist
