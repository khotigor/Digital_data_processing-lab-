"""
Here is lab 3.
Getting a signal + noise mixture
"""

import sys

sys.path.append('../')
from SignalClass import *
from NoiseClass import *

# create signal and noise
signal = Signal(T_MATH, 1, BIAS, FREQUENCY, INITIAL_PHASE, SAMPLING)
noise = Noise(T_MATH, NOISE_RATIO_SIGMA, SAMPLING)

# count cos values of signal and noise
signal.count(True)
noise.count()

# check that signal and Noise are additive
if signal.xs != noise.xs or len(signal.cos_values) != len(noise.cos_values):
    raise ValueError("Signal and Noise are not additive")

print("\n...working on counting a sum of signal and noise")
# count sum of signal and noise
avg_cos = avg_counter(signal.cos_values)
res_cos_values = []
for i in range(len(signal.cos_values)):
    res_cos_values.append(
        float(signal.cos_values[i]) + A_NOISE * float(
            noise.cos_values[i]) - avg_cos)
print("Counting compete")

# plot a part of signal with noise
print("\n...working on plotting")
plot = plotter(DPI, T_BUILD, "Signal+Noise", "t, s", "U, V", -3, 3)
plt.plot(signal.xs, res_cos_values, '.', label="Signal+Noise")
print("Plotting compete")
plot.savefig("{file_name}.png".format(file_name="Signal+Noise"))
print("Saving complete")

# saving point in cvs
print("\n...working on writing cvs")
write_to_csv("pointsFile", signal.xs, res_cos_values)
