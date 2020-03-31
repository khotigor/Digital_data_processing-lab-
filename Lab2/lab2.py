"""
Here is lab 2.
Generation of discrete noise samples.
"""

import sys

sys.path.append('../')
from NoiseClass import *

print("\n...working on plotting discrete noise and writing cvs")
noise = Noise(T_MATH, NOISE_RATIO_SIGMA, SAMPLING)
noise.plot_my_noise()
