import os.path

from music_management.filewriter import write_songs_in_file
from music_management.utils import set_logger_settings, main

if __name__ == '__main__':
    logger = set_logger_settings()
    directory, msc_lib = main()
    write_songs_in_file(os.path.join(directory, "all_songs.txt"), *msc_lib.all_songs)
    logger.info('end.')
