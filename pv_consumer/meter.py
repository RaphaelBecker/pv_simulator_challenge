import publisher


def get_power_per_second(timestamp: int, min_consumption: int, max_consumption: int) -> tuple[int, float]:
    """
    :param timestamp: timestamp in [s]
    :param min_consumption: Minimum power consumption of the measured object by meter
    :param max_consumption: Maximum power consumption of the measured object by meter
    :return: Timestamp - power value pair
    """
    # morning time: from 0am till 5am
    if 0 <= timestamp <= (5 * 60 * 60):
        return timestamp, min_consumption
    # nighttime: from 9pm till 12pm"
    elif (21 * 60 * 60) <= timestamp <= (24 * 60 * 60):
        return timestamp, min_consumption
    else:
        # start inverted parable:   8*60*60 = 28800 sec
        # end inverted parable:     20*60*60 = 72000 sec
        val = round((0.000005 * (- ((timestamp - 53000) * (timestamp - 53000))) + max_consumption), 2)
        if val < min_consumption:
            return timestamp, min_consumption
        else:
            return timestamp, val


def simulate(min_consumption: int, max_consumption: int, from_timestamp=0, to_timestamp=86400, step=1) \
        -> [tuple[int, float]]:
    """
    :param min_consumption: Minimum power consumption of the measured object by meter
    :param
    :param from_timestamp: Min 0 Seconds
    :param to_timestamp: 86400 Seconds for a whole day
    :param step: Inkrement
    :return: Timestamp - power value pair
    """
    simulated_day = []
    for second in range(from_timestamp, to_timestamp, step):
        simulated_day.append(get_power_per_second(second, min_consumption, max_consumption))
    return simulated_day


class Meter:
    def __init__(self, meter_id: str, exchange: str, min_consumption=0, max_consumption=9000):
        """
        :param meter_id: unique meter id for identification
        :param exchange: Name of rabbitMQ exchange where messages will be published to
        :param min_consumption: Minimum power consumption of the measured object by meter
        :param max_consumption: Maximum power consumption of the measured object by meter
        """
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