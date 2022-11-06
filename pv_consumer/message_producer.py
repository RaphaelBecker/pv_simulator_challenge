#!/usr/bin/env python
import meter

print("Started message producer!")
meter_id = input('Enter meter id:\n')
exchange_name = input('Enter exchange name:\n')
Meter = meter.Meter(meter_id, exchange_name)

while True:
    user_input = input("\nWaiting for user input, type: "
                       "\n * '1' to send parts of a day "
                       "\n * '2' send a whole day "
                       "\n * '3' disconnect from exchange "
                       "\n")

    if user_input == "1":
        user_from_timestamp = input("\nEnter from timestamp [s] (int):")
        user_to_timestamp = input("\nEnter to timestamp [s] (int):")
        Meter.publish_partial_simulated_day(from_timestamp=int(user_from_timestamp), to_timestamp=int(user_to_timestamp), step=1)
    if user_input == "2":
        Meter.publish_imulated_day(step=1)
    if user_input == "3":
        Meter.close_connection()
        print("Please exit by CTRL + C")