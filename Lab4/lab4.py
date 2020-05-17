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

w_plus = 0
w_minus = 0
for i in range(len(freq)):
    if freq[i] == round(FREQUENCY, -1):
        w_plus = i
        print("Reference number +w: {w}".format(w=w_plus))
    if freq[i] == -round(FREQUENCY, -1):
        w_minus = i
        print("Reference number -w: {w}".format(w=w_minus))

# Does not work..(
# power_signal = (np.abs(fft_sum[1000]) ** 2 + np.abs(fft_sum[w_minus]) ** 2)
# print("Power")
# print(power_signal)

print("\nDoubled sum of squares 2805 ... 2812 samples is a power:")
i = 2805
power_signal = 0
while i <= 2812:
    power_signal = power_signal + pow(np.abs(fft_sum[i]), 2)
    i = i + 1
power_signal = power_signal * 2
print("{power} \n".format(power=power_signal))

snr = power_signal / (sum([i ** 2 for i in np.abs(fft_sum)]) - power_signal)
print("SNR: {snr}".format(snr=snr))
if not SNR * 0.8 > snr > SNR * 1.2:
    print(
        "The value does not agree with the theoretical. The reason may be" +
        "in the normal distribution and the numpy library (fft function)")

plot_signal = plotter_fft(DPI, freq, fft_signal, 'Signal amplitude spectrum',
                          'f, HZ', 'U, V')
plot_signal.savefig('signal.png')
plt.axis(
    [round(FREQUENCY, -1) - 1000, round(FREQUENCY, -1) + 1000, - 0.02, 0.55])
plot_signal.savefig('signal_small.png')

plot_noise = plotter_fft(DPI, freq, fft_noise, 'Noise amplitude spectrum',
                         'f, HZ', 'U, V')
plot_noise.savefig('noise.png')

plot_sum = plotter_fft(DPI, freq, fft_sum, 'Signal+moise amplitude spectrum',
                       'f, HZ', 'U, V')
plot_sum.savefig('sum.png')
plt.axis(
    [round(FREQUENCY, -1) - 1000, round(FREQUENCY, -1) + 1000, - 0.02, 0.55])
plot_sum.savefig('sum_small.png')

print("\nThe sum of the squares of all samples in the amplitude spectrum of" +
      "the signal + noise mixture:")
sum_fft_sum = 0
for i in range(len(fft_sum)):
    sum_fft_sum = sum_fft_sum + pow(np.abs(fft_sum[i]), 2)
print(sum_fft_sum)
