import sys, os, os.path
from scipy.io import wavfile
import pandas as pd


samrate, data = wavfile.read('./sounds/result.wav')
print('Load is Done! \n')

wavData = pd.DataFrame(data)
wavData = wavData.T
wavData.to_csv("adsfasdfds.csv", mode='w')