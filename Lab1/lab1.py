"""
Here is lab 1.
"""

import sys

sys.path.append('../')
from SignalClass import *

signal = Signal(T_MATH, AMPLITUDE, BIAS, FREQUENCY, INITIAL_PHASE, SAMPLING)

# plot all signal
print("\n...working on plotting signal")
signal.plot_my_signal(T_MATH, "All signal",
                      "All signal", "signalAll", False)

# plot a part of signal
print("\n...working on plotting a part of signal")
signal.plot_my_signal(T_BUILD, "Signal",
                      "Signal", "signal", False)

# plot a discrete signal
print("\n...working on plotting discrete signal and writing cvs")
signal.plot_my_signal(T_BUILD, "Signal",
                      "Discrete", "discrete", True)
