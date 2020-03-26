import csv
import math
import matplotlib.pyplot as plt


def write_to_csv(file_name, data_list):
    points_file = open("{file_name}.csv".format(file_name=file_name), 'w')
    with points_file:
        writer = csv.writer(points_file)
        writer.writerows(data_list)
    print("Writing complete")


def plotter(dpi, time_build, name, x_label, y_label):
    plot = plt.figure(dpi=dpi, figsize=(1080 / dpi, 720 / dpi))
    plt.axis([0, time_build, -1, 2])

    plt.title(name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plot

