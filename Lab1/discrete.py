"""
Here we build a part of discrete signal.
"""

import sys

sys.path.append('../')
from values import *
from SignalClass import *

discrete = Signal(T_MATH, AMPLITUDE, BIAS, FREQUENCY, INITIAL_PHASE, SAMPLING)
discrete.plot_my_signal(DPI, T_MATH, T_BUILD, "Signal", "t, s", "U, V",
                        "Discrete", "Discrete", True, 0)


"""
print("Number of samples = {n_sample}".format(n_sample=len(cos_values)))

print("Zero point = {cos_point_zero}".format(
    cos_point_zero=AMPLITUDE * math.cos(
        2 * math.pi * 0 * FREQUENCY + math.pi * INITIAL_PHASE / 180) + BIAS))

print("\nAverage of signal = {average}".format(
    average=sum((cos_values[i] for i in range(0, len(cos_values)))) / len(
        cos_values)))
print("\n")
"""
