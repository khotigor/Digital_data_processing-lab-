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

print("Number of samples = {n_sample}".format(n_sample=len(cos_values)))

print("Zero point = {cos_point_zero}".format(
    cos_point_zero=AMPLITUDE * math.cos(
        2 * math.pi * 0 * FREQUENCY + math.pi * INITIAL_PHASE / 180) + BIAS))

print("\nAverage of signal = {average}".format(
    average=sum((cos_values[i] for i in range(0, len(cos_values)))) / len(
        cos_values)))
print("\n")


