import random
import sys

sys.path.append('../')
from functions import *
from values import *

plotter_to_work_part = plotter(DPI, T_BUILD, 'NoisePart', "t, s", "U, V")

xs = []
cos_values = []

x = 0.0
data_list = [['t', 'u']]
while x <= T_MATH:
    new_cos_value = random.normalvariate(0, NOISE_RATIO_SIGMA)
    data_list.append([x, new_cos_value])
    cos_values.append(new_cos_value)
    xs.append(x)
    x += math.pow(SAMPLING, -1)

print("Average of noise = {avg}".format(avg=sum(cos_values)/len(cos_values)))

plt.plot(xs, cos_values, '.', label='NoisePart')
plotter_to_work_part.savefig("NoisePart.png")
print("Saving complete")

write_to_csv("pointsFile", data_list)
