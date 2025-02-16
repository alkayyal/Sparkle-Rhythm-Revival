import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
import soundfile as sf

# Given an audio file, return a binary list of whenever the song surpasses 
# the 70th percentile of energy output compared to the average energy of
# the song

def song_decomposition(song_file, threshold, beat_list_length):
    data,samplerate = sf.read(song_file)
    
    beats = []
    total_song_energy = energy_aggregate(data.T[0])
    average_energy = total_song_energy / beat_list_length

    deviance = data.T[0]*data.T[0]
    deviance = deviance.std()

    sample_window = len(data)//beat_list_length

    for i in range(beat_list_length):
        start = i*sample_window
        end = (i+1)*sample_window
        time_snippet = data[start:end].T[0]

        current_energy = energy_aggregate(time_snippet)
        z_score = (current_energy - average_energy) / deviance
        if(z_score >= 0.5):
            beats.append(1)
        else:
            beats.append(0)

    return beats

def energy_aggregate(signal):
    total = np.dot(signal,signal)
    return total

def main():
    song = 'sparkle_music\Beach Bowl Galaxy.flac'

    song_decomposition(song,0,3000)



if __name__=='__main__':
    main()