from functions import *
from values import *

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
        self.xs = None
        self.cos_values = None

    def count(self, discrete):
        xs = []
        cos_values = []

        x = 0.0
        while x <= self.t_math:
            new_cos_value = signal_count(x, self.amplitude, self.frequency,
                                         self.init_phase, self.bias)
            cos_values.append(new_cos_value)
            xs.append(x)

            if discrete:
                x += math.pow(self.sampling, -1)
            else:
                # increased accuracy
                x += math.pow(self.sampling, -1) / 10

        self.xs = xs
        self.cos_values = cos_values

    def plot_my_signal(self, time_build, name, label, file_name,
                       discrete):
        """Method to plot signal"""
        self.count(discrete)
        min_for_plot = min(self.cos_values)
        max_for_lot = max(self.cos_values)
        plot = plotter(DPI, time_build, name, "t, s", "U, V", min_for_plot,
                       max_for_lot)
        if discrete:
            # plot just points
            plt.plot(self.xs, self.cos_values, '.', label=label)
        else:
            # plot lines
            plt.plot(self.xs, self.cos_values, linestyle='solid', label=label)
            print("Plotting complete")

        # save png
        plot.savefig("{file_name}.png".format(file_name=file_name))
        print("Saving complete")

        if discrete:
            write_to_csv("pointsFile", self.xs, self.cos_values)

            print("\n...counting some results")
            print("Number of samples = {n_sample}".format(
                n_sample=len(self.cos_values)))

            print("Zero point = {cos_point_zero}".format(
                cos_point_zero=zero_signal(self.amplitude, self.frequency,
                                           self.init_phase, self.bias)))
            print(avg_counter(self.cos_values))
