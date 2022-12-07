# Used in order to specify a specific and generate a csv for testing purposes

from scipy.io import wavfile
import pandas as pd

def createCSV(input):
    samrate, data = wavfile.read('./sounds/weather.wav')
    wavData = pd.DataFrame(data)
    wavData.to_csv(input, mode='w')

createCSV("result.csv")