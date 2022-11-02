#!/usr/bin/env python
import csv
import json
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


def save_to_csv(messages: [dict]):
    filename = 'messages.csv'
    with open(filename, 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file,
                            fieldnames=messages[0].keys(),

                            )
        fc.writeheader()
        fc.writerows(messages)


print("Started simulator!")
exchange_name = input('Enter exchange name:\n')
Listener = listener.Listener(exchange_name)
Listener.listen_for_packages()
while True:
        user_input = input("\nWaiting for user input, type: "
                           "\n * a to show received messages "
                           "\n * b for delete received messages "
                           "\n * c compute solar panel - meter difference "
                           "\n * d save messages to csv "
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
                    panel_value = solar_pannel.get_solar_power(message_dict['timestamp'])
                    panel_meter_diff = round((panel_value - message_dict['meter_value']), 2)
                    print(f"ts: {message_dict['timestamp']} diff: {panel_meter_diff}")
            if user_input == "d":
                cast_buffer = []
                for message in Listener.received_messages:
                    message_dict = json.loads(message.decode())
                    panel_value = round(solar_pannel.get_solar_power(message_dict['timestamp']), 2)
                    panel_meter_diff = round((panel_value - message_dict['meter_value']), 2)
                    message_dict['panel_value'] = panel_value
                    message_dict['panel_meter_diff'] = panel_meter_diff
                    cast_buffer.append(message_dict)
                save_to_csv(cast_buffer)
                print("dumped to csv!")