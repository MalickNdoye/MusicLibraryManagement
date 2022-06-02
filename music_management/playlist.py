

class Playlist:

    def __init__(self, pl_id: int = 0, name: str = ''):
        self.id = pl_id
        self.name = name
        self.playlist = []

    def __str__(self):
        return str(self.id) + str(self.playlist)

    def add_music(self, music: MusicTitle) -> None:
        self.playlist.append(music)

    def get_playlist(self) -> list:
        return self.playlist

    @property
    def size(self) -> int:
        return len(self.playlist)

