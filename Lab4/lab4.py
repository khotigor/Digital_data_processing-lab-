import numpy
import sys

sys.path.append('../')
from SignalClass import *
from NoiseClass import *

list_signal = (read_from_csv("../Lab1/pointsFile"))
list_noise = (read_from_csv("../Lab2/pointsFile"))
list_sum = (read_from_csv("../Lab3/pointsFile"))

print(numpy.fft.fft(parser(list_sum, 0)))

# plot = plotter(DPI, T_BUILD, "Signal+Noise", "t, s", "A, Hz", 0, 1)

