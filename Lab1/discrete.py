import matplotlib.pyplot as plt
import math
from values import *

discrete = plt.figure(dpi=DPI, figsize=(1080 / DPI, 720 / DPI))
plt.axis([0, T_BUILD, -1, 2])

plt.title('Discrete')
plt.xlabel('t, s')
plt.ylabel('U, V')

xs = []
cos_values = []

x = 0.0
while x <= T_BUILD:
    cos_values += [
        AMPLITUDE * math.cos(
            2 * math.pi * x * FREQUENCY + math.pi * INITIAL_PHASE / 180)
        + BIAS]
    xs += [x]
    x += math.pow(SAMPLING, -1)

plt.plot(xs, cos_values, '.', label='discrete')

discrete.savefig('discrete.png')
