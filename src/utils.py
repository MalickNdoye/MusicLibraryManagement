import glob
import os

cs_title = {'001.txt': 'Lost Imagination',
            '002.txt': 'Dust to Discovery',
            '003.txt': 'Remember Time',
            '004.txt': 'Beyond Dawn',
            '005.txt': 'Lucid Emotion',
            '006.txt': 'After Nothing',
            '007.txt': 'Blurred Radiance',
            '008.txt': 'default_title',
            '009.txt': 'Another Wanderer',
            '010.txt': 'Light Dreams',
            '011.txt': 'Goodbye Embrace',
            '012.txt': 'For Those Dreams',
            '013.txt': 'Locked Inside',
            '014.txt': 'Best of the Best',
            '015.txt': 'Our World Anew',
            '016.txt': 'Bring Me Those Days',
            '017.txt': 'Light the Way',
            '018.txt': 'Arcane Stars',
            '019.txt': 'Light Ripple',
            '020.txt': 'Moment Alone',
            '021.txt': 'Interstellar Escape',
            '022.txt': 'Still Beauty',
            '023.txt': 'Falling Through',
            '024.txt': 'Discover Wonder',
            '025.txt': 'Follow The Clouds',
            '026.txt': 'Anywhere From The Past',
            '027.txt': 'First We Fly',
            '028.txt': 'Hollow Embrace',
            '029.txt': 'Moonlight Passage',
            '030.txt': 'Tomorrow Farewell - Vocal Chillout Mix',
            '031.txt': 'A Night In The Stars',
            '032.txt': 'Black Dawn',
            '033.txt': 'Alone On Earth',
            '034.txt': 'Light Synergy'}


def append_title_to_file(file_name):
    path = os.path.join(os.curdir, '..', 'resources', 'Title')
    filepath = os.path.join(path, file_name)
    with open(filepath, 'a') as file:
        line = '\n\nTitle : ' + cs_title[file_name] + '\n'
        print(f'Writing "{line}" in "{filepath}"')
        file.write(line)
    print('end.')


def update_compilation_title():
    cs_dir = os.path.join('D:\\', 'Music', 'Classement par Genre', 'Ambient', 'Chillout Soundscapes', '*.mp3')
    cs_songs = glob.glob(cs_dir)
    base_name = []
    song_id = []
    for path in cs_songs:
        filename = os.path.basename(path).split('.')
        name = filename[0].replace('__', '_')
        playlist_id = filename[0].split('_', 2)[0]
        base_name.append(name[4:].replace('_', ' '))
        song_id.append(playlist_id)
    assert len(base_name) == len(song_id)
    for i in range(len(song_id)):
        cs_title[f"{song_id[i]}.txt"] = base_name[i]
