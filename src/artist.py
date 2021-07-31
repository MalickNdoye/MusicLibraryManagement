from src.music import MusicTitle


class Artist:

    def __init__(self, name='', msc=MusicTitle(artist='')):
        self.name = name
        self.titles = {msc.title: msc}

    def add_song(self, msc_obj):
        if isinstance(msc_obj, MusicTitle):
            if self.titles.get(msc_obj.title, None) is None:
                self.titles[msc_obj.title] = msc_obj
            else:
                self.titles[msc_obj.title].duplicated = True
                self.titles[msc_obj.title].add_playlist_presence(*msc_obj.get_playlist_presence())

    def get_duplicates(self):
        duplicates = []
        for title in self.titles:
            if self.titles[title].duplicated is True:
                duplicates.append(self.titles[title])
        return duplicates

    def get_songs(self):
        return self.titles.values()

    @property
    def nb_songs(self):
        return len(self.titles)

    @property
    def nb_duplicate(self):
        nb = 0
        for msc in self.titles.values():
            if msc.duplicated is True:
                nb += 1
        return nb
