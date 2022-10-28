import sys
import time


# 1 day = 24h -> 24h*60min*60sec =

def get_power(seconds: int) -> float:
    if not (0 <= seconds <= (24*60*60)):
        day_seconds_error = ValueError('One day has 0 till 86400 seconds!')
        raise day_seconds_error
    # morning time: from 0am till 5am return 0
    if 0 <= seconds <= (5 * 60 * 60):
        return 0
    # night time: from 9pm till 12pm return 0
    elif (21 * 60 * 60) <= seconds <= (24 * 60 * 60):
        return 0
    else:
        # start inverted parable:   8*60*60 = 28800 sec
        # end inverted parable:     20*60*60 = 72000 sec
        val = round((0.000010 * (- ((seconds - 53000) * (seconds - 53000))) + 3250), 2)
        if val < 0:
            return 0
        else:
            return val

def meter() -> int:
    print("I am meter")
    return 0


if __name__ == '__main__':
    meter()
