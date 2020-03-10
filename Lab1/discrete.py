import math

import matplotlib.pyplot as plt
import csv
from values import *

discrete = plt.figure(dpi=DPI, figsize=(1080 / DPI, 720 / DPI))
plt.axis([0, T_BUILD, -1, 2])

plt.title('Discrete')
plt.xlabel('t, s')
plt.ylabel('U, V')

xs = []
cos_values = []

x = 0.0
dataList = [['t', 'u']]
while x <= T_MATH:
    new_cos_value = AMPLITUDE * math.cos(
        2 * math.pi * x * FREQUENCY + math.pi * INITIAL_PHASE / 180) + BIAS
    cos_values.append(new_cos_value)
    dataList.append([x, new_cos_value])
    xs += [x]
    x += math.pow(SAMPLING, -1)

pointsFile = open('pointsFile.csv', 'w')
with pointsFile:
    writer = csv.writer(pointsFile)
    writer.writerows(dataList)
print("Writing complete")

plt.plot(xs, cos_values, '.', label='discrete')
print("Plotting complete")

discrete.savefig('discrete.png')
print("Saving complete")
