#!/usr/bin/env python
import csv
import json
import os
import time

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


def computer_panel_meter_diff(timestamp, meter_value):
    # positive if enough energy is produced by the panel:
    return meter_value - solar_pannel.get_solar_power(timestamp)


print("Started simulator!")
exchange_name = input('Enter exchange name:\n')
Listener = listener.Listener(exchange_name)
Listener.listen_for_packages()
while True:
        user_input = input("\nWaiting for user input, type: "
                           "\n * a to show received messages "
                           "\n * b for delete received messages "
                           "\n * c compute solar panel - meter difference "
                           "\n * d for saving messages to csv "
                           "\n")
        if Listener.receiving:
            print("Listener receiving messages right now. Waiting for end of batch, please wait!")
        else:
            if user_input == "a":
                for message in Listener.received_messages:
                    print(message)
            if user_input == "b":
                Listener.delete_messages()
                print("deleted:")
                print(Listener.received_messages)
            if user_input == "c":
                for message in Listener.received_messages:
                    message_dict = json.loads(message.decode())
                    print(f"ts: {message_dict['timestamp']} {round(computer_panel_meter_diff(message_dict['timestamp'], message_dict['meter_value']), 2)}")
            if user_input == "d":
                print("dumped to csv!")

