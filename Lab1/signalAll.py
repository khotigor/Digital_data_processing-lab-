"""
Here we build all signal.
"""

import sys

sys.path.append('../')
from values import *
from SignalClass import *

signalAll = Signal(T_MATH, AMPLITUDE, BIAS, FREQUENCY, INITIAL_PHASE, SAMPLING)
signalAll.plot_my_signal(DPI, T_MATH, T_MATH, "All signal", "t, s", "U, V",
                         "All signal", "signalAll", True, False)
