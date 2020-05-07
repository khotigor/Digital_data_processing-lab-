import numpy as np
import sys

sys.path.append('../')
from NoiseClass import *

list_signal = (read_from_csv("../Lab1/pointsFile"))
for i in range(len(list_signal)):
    list_signal[i] = float(list_signal[i][1])
list_noise = (read_from_csv("../Lab2/pointsFile"))
for i in range(len(list_noise)):
    list_noise[i] = float(list_noise[i][1])
list_sum = (read_from_csv("../Lab3/pointsFile"))
for i in range(len(list_sum)):
    list_sum[i] = float(list_sum[i][1])

del list_signal[0]
del list_noise[0]
del list_sum[0]

fft_signal = np.fft.fft(list_signal)
fft_noise = np.fft.fft(list_noise)
fft_sum = np.fft.fft(list_sum)

freq = np.fft.fftfreq(10000, 0.00001)

print(len(freq))
print(len(fft_signal))

w_plus = 0
w_minus = 0
for i in range(len(freq)):
    if freq[i] == round(FREQUENCY, -1):
        w_plus = i
        print("Reference number +w: {w}".format(w=w_plus))
    if freq[i] == -round(FREQUENCY, -1):
        w_minus = i
        print("Reference number -w: {w}".format(w=w_minus))

power_signal = (np.abs(fft_sum[1000]) ** 2 + np.abs(fft_sum[w_minus]) ** 2)
snr = power_signal*35 / (sum([i ** 2 for i in np.abs(fft_sum)]) - power_signal)
print("SNR: {snr}".format(snr=snr))

plot_signal = plotter_fft(DPI, freq, fft_signal, 'Signal amplitude spectrum',
                          'f, HZ', 'U, V')
plot_signal.savefig('signal.png')
plt.axis([round(FREQUENCY, -1)-1000, round(FREQUENCY, -1)+1000, - 0.02, 0.55])
plot_signal.savefig('signal_small.png')


plot_noise = plotter_fft(DPI, freq, fft_noise, 'Signal amplitude noise',
                         'f, HZ', 'U, V')
plot_noise.savefig('noise.png')

plot_sum = plotter_fft(DPI, freq, fft_sum, 'Signal amplitude signal+moise',
                       'f, HZ', 'U, V')
plot_sum.savefig('sum.png')
plt.axis([round(FREQUENCY, -1)-1000, round(FREQUENCY, -1)+1000, - 0.02, 0.55])
plot_sum.savefig('sum_small.png')




