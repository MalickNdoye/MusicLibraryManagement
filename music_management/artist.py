from music_management import logger
from music_management.music import MusicTitle


class Artist:

    def __init__(self, name='', msc=MusicTitle(artist='')):
        self.name = name
        self.titles = {msc.title: msc}
        logger.info('Creating %s as Artist.',  self.name)

    def add_song(self, msc_obj):
        if isinstance(msc_obj, MusicTitle):
            if self.titles.get(msc_obj.title, None) is None:
                self.titles[msc_obj.title] = msc_obj
                logger.info('Adding the song (%s) to %s catalog', msc_obj.title, self.name)
            else:
                self.titles[msc_obj.title].duplicated = True
                for pl_name in msc_obj.get_playlist_presence():
                    self.titles[msc_obj.title].add_playlist_presence(pl_name=pl_name,
                                                                     timestamp=msc_obj.in_playlist[pl_name])

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
