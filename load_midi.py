import midi_manipulation
import glob
from tqdm import tqdm
import numpy as np

def get_songs(path):
    files = glob.glob('{}/*.mid*'.format(path))
    songs = []
    for f in tqdm(files):
        try:
            song = np.array(midi_manipulation.midiToNoteStateMatrix(f))
            if np.array(song).shape[0] > 50:
                songs.append(song)
        except Exception as e:
            raise e           
    return songs

songs = get_songs('Pop_Music_Midi') #These songs have already been converted from midi to msgpack
print( len(songs)+ " songs processed")