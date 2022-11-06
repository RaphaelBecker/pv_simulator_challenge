#!/usr/bin/env python
import csv
import json

import solar_pannel
import listener


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
                           "\n * '1' to show received messages "
                           "\n * '2' for delete received messages "
                           "\n * '3' compute solar panel - meter difference "
                           "\n * '4' save messages to csv "
                           "\n")
        if Listener.receiving:
            print("Listener receiving messages right now. Waiting for end of batch, please wait!")
        else:
            if user_input == "1":
                for message in Listener.received_messages:
                    print(message)
            if user_input == "2":
                Listener.delete_messages()
                print("deleted:")
                print(Listener.received_messages)
            if user_input == "3":
                for message in Listener.received_messages:
                    message_dict = json.loads(message.decode())
                    panel_value = solar_pannel.get_solar_power(message_dict['timestamp'])
                    panel_meter_diff = round((panel_value - message_dict['meter_value']), 2)
                    print(f"ts: {message_dict['timestamp']} diff: {panel_meter_diff}")
            if user_input == "4":
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