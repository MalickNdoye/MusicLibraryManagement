

class MusicTitle:

    def __init__(self, artist='', title=''):
        self.artist = artist
        self.title = title
        self.in_playlist = {}
        self.duplicated = False

    def __str__(self):
        basic_format = '{:<35}| {:<36}| {}'
        pp = ""
        for pl in self.in_playlist:
            one_play = pl + '('
            for tm in self.in_playlist[pl]:
                one_play += f'{tm//60:02}:{tm%60:02}, '
            one_play = one_play[:-2] + ')'
            pp += one_play + ' - '
        pp = pp[:-3]
        return basic_format.format(self.artist, self.title, pp)
        # return self.artist + '\t|\t' + self.title + '\t| playlist presence :\t' + str(self.in_playlist)

    def add_playlist_presence(self, pl_name, timestamp):
        if isinstance(timestamp, list):
            for tms in timestamp:
                self.add_playlist_presence(pl_name=pl_name, timestamp=tms)
        else:
            if self.in_playlist.get(pl_name, None) is not None:
                self.in_playlist[pl_name].append(timestamp)
            else:
                self.in_playlist[pl_name] = [timestamp]

    def get_playlist_presence(self):
        return self.in_playlist
