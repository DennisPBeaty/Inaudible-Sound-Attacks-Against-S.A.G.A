import sys
import os
import platform
from playsound import *
import time
from pydub import AudioSegment
import numpy as np

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from scipy.io import wavfile
import pandas as pd

import csv
import wave
import contextlib

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

def playDevice():
    #Create Wave File
    return AudioSegment.from_wav('./sounds/Hey_Google.wav')

def createCSV(input):
    samrate, data = wavfile.read('./sounds/result.wav')
    wavData = pd.DataFrame(data)
    wavData.to_csv(input, mode='w')

 #Create Wave File
sound1 = AudioSegment.from_wav('./sounds/Hey_Google.wav')
sound2 = AudioSegment.from_wav("./sounds/weather.wav")
combined_sounds = sound1 + sound2
combined_sounds.export("./sounds/result.wav", format="wav")

#Edit the audio for AM Modulation
with wave.open("./sounds/result.wav", "rb") as wave_file:
        # This is the Samples per second SPS var
        sample_rate = wave_file.getframerate()
        print(sample_rate)
    
with contextlib.closing(wave.open("./sounds/result.wav",'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration_s = frames / float(rate)
    print(duration_s)

createCSV("sample.csv")

wav_file = []
with open('sample.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
      wav_file.append(float(row[1]))

#--------------------------------------------------------------------------------------------------
carrier_hz = 440.0
modulator_hz = 0.25
ac = 1.0
ka = 0.25

# Properties of the wav
sps = 44100    # DON'T change

# Calculate the sine wave
t_samples = np.arange(sps * duration_s)
carrier = np.sin(2 * np.pi * carrier_hz * t_samples / sps)
print(carrier)

# Modulate the carrier
#modulator = np.sin(2 * np.pi * modulator_hz * t_samples / sps)
modulator = np.array(wav_file)
envelope = ac * (1.0 + ka * modulator)

modulated = envelope * carrier[:len(envelope)]

# Write the wav file
modulated *= 0.3
modulated_ints = np.int16(modulated * 32767)
write('amplitude-modulation.wav', sps, modulated_ints)

#--------------------------------------------------------------------------------------------------

createCSV("result.csv")