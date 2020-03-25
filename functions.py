import csv


def write_to_csv(file_name, data_list):
    points_file = open("{file_name}.csv".format(file_name=file_name), 'w')
    with points_file:
        writer = csv.writer(points_file)
        writer.writerows(data_list)
    print("Writing complete")
