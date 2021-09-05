import os.path

from music_management.filewriter import write_songs_in_file, write_songs_in_csv_file
from music_management.utils import set_logger_settings, main

if __name__ == '__main__':
    logger = set_logger_settings()
    directory, msc_lib = main()
    write_songs_in_file(os.path.join(directory, "duplicated_songs.txt"), *msc_lib.get_duplicates())
    write_songs_in_csv_file(os.path.join(directory, "duplicated_songs.csv"), *msc_lib.get_duplicates())

    logger.info('end.')
