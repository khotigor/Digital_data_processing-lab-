"""
Here we build a part of discrete signal.
"""

import sys

sys.path.append('../')
from values import *
from SignalClass import *

discrete = Signal(T_MATH, AMPLITUDE, BIAS, FREQUENCY, INITIAL_PHASE, SAMPLING)
discrete.plot_my_signal(DPI, T_MATH, T_BUILD, "Signal", "t, s", "U, V",
                        "Discrete", "Discrete", True, 0.5)

