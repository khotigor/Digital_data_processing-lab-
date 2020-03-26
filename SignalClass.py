import math
import random

from functions import *


class Signal(object):
    """It's my signal"""

    def __init__(self, t_math, amplitude, bias, frequency, init_phase,
                 sampling):
        """Constructor"""
        self.t_math = t_math  # time of modelling
        self.amplitude = amplitude  # amplitude of signal
        self.bias = bias  # bias of signal
        self.frequency = frequency  # frequency of signal
        self.init_phase = init_phase  # init_phase of signal
        self.sampling = sampling  # sampling of signal

    def plot_my_signal(self, dpi, time_math, time_build, name, x_label,
                       y_label, label, file_name, discrete,
                       noise_ratio_sigma):
        """Method to plot signal"""
        plotter_to_work = plotter(dpi, time_build, name, x_label, y_label)
        xs = []
        cos_values = []

        x = 0.0
        data_list = [['t', 'u']]
        while x <= time_math:
            new_cos_value = [
                self.amplitude * math.cos(
                    2 * math.pi * x * self.frequency + math.pi *
                    self.init_phase / 180) + self.bias +
                random.normalvariate(0, noise_ratio_sigma)]
            data_list.append([x, new_cos_value])
            cos_values.append(new_cos_value)
            xs.append(x)

            if discrete:
                x += math.pow(self.sampling, -1)
            else:
                x += 0.000001

        if discrete:
            plt.plot(xs, cos_values, '.', label=label)
        else:
            plt.plot(xs, cos_values, linestyle='solid', label=label)
            print("Plotting complete")

        plotter_to_work.savefig("{file_name}.png".format(file_name=file_name))
        print("Saving complete")

        # should be done normally ...once...
        if discrete:
            write_to_csv("pointsFile", data_list)
            print("Number of samples = {n_sample}".format(
                n_sample=len(cos_values)))

            # i will somehow make a separate function, maybe
            print("Zero point = {cos_point_zero}".format(
                cos_point_zero=self.amplitude * math.cos(
                    2 * math.pi * 0 * self.frequency + math.pi *
                    self.init_phase / 180) + self.bias))
