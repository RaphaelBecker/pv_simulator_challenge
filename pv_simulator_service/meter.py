#!/usr/bin/env python
from pv_simulator_service import publisher


def get_power_per_second(second: int, min_consumption: int, max_consumption: int) -> tuple[int, float]:
    # morning time: from 0am till 5am
    if 0 <= second <= (5 * 60 * 60):
        return second, min_consumption
    # nighttime: from 9pm till 12pm"
    elif (21 * 60 * 60) <= second <= (24 * 60 * 60):
        return second, min_consumption
    else:
        # start inverted parable:   8*60*60 = 28800 sec
        # end inverted parable:     20*60*60 = 72000 sec
        val = round((0.000005 * (- ((second - 53000) * (second - 53000))) + max_consumption), 2)
        if val < min_consumption:
            return second, min_consumption
        else:
            return second, val


def simulate(min_consumption: int, max_consumption: int, from_timestamp=0, to_timestamp=86400, step=1) \
        -> [tuple[int, float]]:
    simulated_day = []
    for second in range(from_timestamp, to_timestamp, step):
        simulated_day.append(get_power_per_second(second, min_consumption, max_consumption))
    return simulated_day


class Meter:
    def __init__(self, meter_id: str, exchange: str, min_consumption=0, max_consumption=3250):
        self.meter_id = meter_id
        self.min_consumption = min_consumption
        self.max_consumption = max_consumption
        self.publisher = publisher.Publisher(exchange=exchange, exchange_type="fanout")

    def publish_simulated_day(self, step):
        simulated_day = simulate(self.min_consumption, self.max_consumption, step)
        for sim_tuple in simulated_day:
            self.publisher.publish_pv_value(self.meter_id, sim_tuple[0], sim_tuple[1], False)
        # EOM batch
        self.publisher.publish_pv_value(self.meter_id, 0, 0, True)

    def publish_partial_simulated_day(self, from_timestamp, to_timestamp, step):
        partial_simulated_day = simulate(self.min_consumption, self.max_consumption, from_timestamp, to_timestamp, step)
        for sim_tuple in partial_simulated_day:
            self.publisher.publish_pv_value(self.meter_id, sim_tuple[0], sim_tuple[1], False)
        # EOM batch
        self.publisher.publish_pv_value(self.meter_id, 0, 0, True)

    def close_connection(self):
        self.publisher.close_connection()