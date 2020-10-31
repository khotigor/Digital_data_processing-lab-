from scipy.io import wavfile
from scipy import signal

import sys

sys.path.append('../')
from SignalClass import *

audiofile = 'sample13.wav'

rate, data = wavfile.read(audiofile)
duration = data.shape[0] / rate

print(data.shape[0])
print(rate)

freq1 = np.fft.fftfreq(data.shape[0], 1 / rate)
data_signal = np.fft.fft(data)

# find subcarrier frequency on graphics
plt.plot(freq1, np.abs(data_signal))
plt.xlabel(u'frequency Hz')
plt.ylabel(u'Amplitude')
plt.title(u'Amplitude spectrum of the signal')
plt.grid(True)
plt.savefig(fname='graphics/1', fmt='png')
plt.axis([42000, 46000, - 0.02, 10000])
plt.savefig(fname='graphics/2', fmt='png')
plt.close()

subcarrier_frequency = 44000

b, a = signal.butter(10, 20000, btype='lowpass', fs=rate)
additive_component = signal.filtfilt(b, a, data)

b, a = signal.butter(10, 20000, btype='highpass', fs=rate)
difference_component = signal.filtfilt(b, a, data)

amplitude_spectrum_3 = plotter_fft(DPI, freq1,
                                 np.abs(np.fft.fft(additive_component)),
                                 'Amplitude spectrum of the additive signal component',
                                 'frequency, HZ', 'Amplitude')
amplitude_spectrum_3.savefig('graphics/3.png')

amplitude_spectrum_4 = plotter_fft(DPI, freq1,
                                 np.abs(np.fft.fft(difference_component)),
                                 'Amplitude spectrum of the signal difference component',
                                 'frequency, HZ', 'Amplitude')
amplitude_spectrum_4.savefig('graphics/4.png')

t = 0
for i in range(0, len(difference_component)):
    difference_component[i] = difference_component[i] * math.cos(
        2 * math.pi * t * subcarrier_frequency)
    t = t + 1 / rate

b, a = signal.butter(10, 15000, btype='lowpass', fs=rate)
difference_component = signal.filtfilt(b, a, difference_component)

for i in range(0, len(difference_component)):
    difference_component[i] = 2 * difference_component[i]

first_channel = np.zeros(len(data))
second_channel = np.zeros(len(data))

for i in range(0, len(data)):
    first_channel[i] = (additive_component[i] + difference_component[i]) / 2
    second_channel[i] = (additive_component[i] - difference_component[i]) / 2

wavfile.write('13_ch1.wav', rate, first_channel)
wavfile.write('13_ch2.wav', rate, second_channel)
