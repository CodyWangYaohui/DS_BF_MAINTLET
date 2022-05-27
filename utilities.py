import BeamformingBasics as bf
import scipy.io.wavfile as wavfile
import numpy as np 
import sounddevice as sd


'''
This helper function is for playing the audio in format of numpy array

processed_source is the array to play

sample_freq is the sampling frequency

very noisy
'''
def play_audio(processed_source, sample_freq):
    sd.play(processed_source, samplerate=sample_freq)
