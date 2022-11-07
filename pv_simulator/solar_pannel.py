import sys
import time

# 1 day = 24h -> 24h*60min*60sec

out_of_bound_error = ValueError(f"ValueError: One day has 0 till 86400 seconds. Input value out of bound.")
type_error = TypeError(f"TypeError: Seconds not of type int.")
max_power = 3250


def get_solar_power(timestamp: int) -> float:
    """
    :param timestamp: Timestamp in [s]
    :return: Power value in [W]
    """
    if not type(timestamp) == int:
        raise type_error
    if not (0 <= timestamp <= (24 * 60 * 60)):
        raise out_of_bound_error
    # morning time: from 0am till 5am return 0
    if 0 <= timestamp <= (5 * 60 * 60):
        return 0
    # night time: from 9pm till 12pm return 0
    elif (21 * 60 * 60) <= timestamp <= (24 * 60 * 60):
        return 0
    else:
        # start inverted parable:   8*60*60 = 28800 sec
        # end inverted parable:     20*60*60 = 72000 sec
        val = round((0.000010 * (- ((timestamp - 53000) * (timestamp - 53000))) + max_power), 2)
        if val < 0:
            return 0
        else:
            return val
