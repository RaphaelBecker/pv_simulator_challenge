#!/usr/bin/env python
import csv
import os
import solar_pannel
import listener


def load_csv() -> []:
    messages = []
    filename = 'messages.csv'
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for rows in reader:
                messages.append(rows)
    else:
        save_to_csv([])
    return messages


def save_to_csv(messages: [tuple]):
    filename = 'messages.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(messages)



print("Started simulator!")
print("Enter meter id:")
print("Enter meter exchange:")
SolarPanel = solar_pannel.SolarPanel()
Listener = listener.Listener("meter_01_exchange", "fanout")
Listener.listen_for_packages()
print(Listener.received_messages)

