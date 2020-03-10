import matplotlib.pyplot as plt
import math
from values import *

signal = plt.figure(dpi=DPI, figsize=(1080 / DPI, 720 / DPI))
plt.axis([0, T_MATH, -1, 2])

plt.title('SignalAll')
plt.xlabel('t, s')
plt.ylabel('U, V')

xs = []
cos_values = []

x = 0.0
while x <= T_MATH:
    cos_values += [
        AMPLITUDE * math.cos(
            2 * math.pi * x * FREQUENCY + math.pi * INITIAL_PHASE / 180)
        + BIAS]
    xs += [x]
    x += 0.000001

plt.plot(xs, cos_values, linestyle='solid', label='Signal')
print("Plotting complete")

signal.savefig('signalAll.png')
print("Saving complete")

print("Initial phase = {ph}".format(ph=math.pi * INITIAL_PHASE))
print("Frequency = {fr}".format(fr=FREQUENCY))
