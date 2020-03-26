"""
Here we build a part of signal.
"""

import sys

sys.path.append('../')
from values import *
from SignalClass import *


signal = Signal(T_MATH, AMPLITUDE, BIAS, FREQUENCY, INITIAL_PHASE, SAMPLING)
signal.plot_my_signal(DPI, T_BUILD, T_BUILD, "Signal", "t, s", "U, V",
                         "Signal", "signal", False, 0.5)
