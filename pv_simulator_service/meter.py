import math

def simulate_day_power_consumption(min_consumption: int, max_consumption: int) -> [()]:
    simulated_power_consumption = []
    for seconds in range(0, 86400, 1):
        # morning time: from 0am till 5am
        if 0 <= seconds <= (5 * 60 * 60):
            simulated_power_consumption.append((seconds, min_consumption))
        # nighttime: from 9pm till 12pm"
        elif (21 * 60 * 60) <= seconds <= (24 * 60 * 60):
            simulated_power_consumption.append((seconds, min_consumption))
        else:
            # start inverted parable:   8*60*60 = 28800 sec
            # end inverted parable:     20*60*60 = 72000 sec
            val = round((0.000005 * (- ((seconds - 53000) * (seconds - 53000))) + max_consumption), 2)
            if val < min_consumption:
                simulated_power_consumption.append((seconds, min_consumption))
            else:
                simulated_power_consumption.append((seconds, val))
    return simulated_power_consumption
