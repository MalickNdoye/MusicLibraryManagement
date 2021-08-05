

class Playlist:

    def __init__(self, pl_id=0, name=''):
        self.id = pl_id
        self.name = name
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

