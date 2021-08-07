from music_management import logger


def write_songs_in_file(filepath, *songs):
    logger.info('Opening and writing into file : ' + filepath)
    with open(filepath, 'w', encoding='utf-8') as file:
        lines = []
        for song in songs:
            lines.append(str(song) + '\n')
        file.writelines(lines)
    logger.info('Closing file : ' + filepath)