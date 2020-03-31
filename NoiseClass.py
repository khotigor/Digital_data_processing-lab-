from functions import *
from values import *


class Noise(object):

    def __init__(self, t_math, amplitude, sampling):
        """Constructor"""
        self.t_math = t_math  # time of modelling
        self.amplitude = amplitude  # amplitude of noise
        self.sampling = sampling  # sampling of noise
        self.xs = None
        self.cos_values = None

    def count(self):
        xs = []
        cos_values = []

        x = 0.0
        while x <= self.t_math:
            new_cos_value = normal_random(self.amplitude)
            cos_values.append(new_cos_value)
            xs.append(x)
            x += math.pow(self.sampling, -1)
        self.xs = xs
        self.cos_values = cos_values

    def plot_my_noise(self):
        self.count()
        min_for_plot = float(min(self.cos_values))
        max_for_lot = float(max(self.cos_values))

        plot = plotter(DPI, T_BUILD, 'Noise', "t, s", "U, V", min_for_plot,
                       max_for_lot)

        plt.plot(self.xs, self.cos_values, '.', label='NoisePart')
        plot.savefig("NoisePart.png")
        print("Saving complete")

        write_to_csv("pointsFile", self.xs, self.cos_values)

        print("\n...counting some results")
        avg = avg_counter(self.cos_values)
        print("Average of noise = {avg}".format(avg=avg))
        d = 0
        for i in self.cos_values:
            d = d + pow((i - avg), 2)
        d = d / (len(self.cos_values) - 1)
        print("Dispersion of noise = {d}".format(d=d))
