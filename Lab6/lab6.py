from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal
import scipy

audiofile = 'sample13.wav'

def filter(data, rate, cutoff, filter_type, order):
    b, a = signal.butter(order, cutoff, btype=filter_type, fs=rate)
    return signal.filtfilt(b, a, data)

def plot(freq, data, x1, x2, y1, y2, i):
    plt.plot(freq, np.abs(np.fft.fft(data)))
    plt.xlabel(u'Частота, Гц')
    plt.ylabel(u'Амплитуда')
    plt.title(u'Амплитудный спектр сигнала')
    plt.grid(True)
    plt.axis([x1, x2, y1, y2])
    plt.savefig(fname=f"graphics/{i}", fmt='png')
    plt.close()

rate, data = wavfile.read(audiofile)
duration = data.shape[0] / rate

print(data.shape[0])
print(rate)

freq = np.fft.fftfreq(data.shape[0], 1 / rate)
plot(freq, data, -12000, 12000, -0.5, 80000, 1)

data = filter(data, rate, 10000, 'lowpass', 20)
plot(freq, data, -8000, 8000, -0.5, 60000, 2)
wavfile.write('filtered1.wav', rate, data)

data = filter(data, rate, 6000, 'lowpass', 20)
plot(freq, data, -1000, 1000, -0.5, 4000, 3)
wavfile.write('filtered2.wav', rate, data)
