

def write_songs_in_file(filepath, *songs):
    with open(filepath, 'w', encoding='utf-8') as file:
        lines = []
        for song in songs:
            lines.append(str(song) + '\n')
        file.writelines(lines)