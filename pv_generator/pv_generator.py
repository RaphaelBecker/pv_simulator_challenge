import csv
import os


def load_csv() -> []:
    no_matching_radars = []
    filename = 'noMatchingRadars.csv'
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for rows in reader:
                no_matching_radars.append(rows)
                no_matching_radars = no_matching_radars[0]
    else:
        save_to_csv([])
    return no_matching_radars


def save_to_csv(latest_no_matching_radars):
    filename = 'noMatchingRadars.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(latest_no_matching_radars)
