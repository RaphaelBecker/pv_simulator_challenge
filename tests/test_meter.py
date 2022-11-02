import unittest
import matplotlib.pyplot as plt

from pv_simulator_service import meter


class TestMeter(unittest.TestCase):

    def test_meter_partial(self):
        # start listener first!
        Meter = meter.Meter("meter_01", "meter")
        Meter.publish_partial_simulated_day(from_timestamp=40000, to_timestamp=50000, step=1)
        Meter.close_connection()

    def test_meter_whole_day(self):
        # start listener first!
        Meter = meter.Meter("meter_01", "meter_01_exchange")
        Meter.publish_simulated_day(step=1)
        Meter.close_connection()

    def test_pv_generation(self):
        # input values are positive from 0 till 86400 for a whole day
        hours = []
        simulated_power_consumption = meter.simulate(min_consumption=0, max_consumption=9000)
        # Plot values for better visual understanding of the values:
        plt.rcParams["figure.autolayout"] = True
        plt.plot(*zip(*simulated_power_consumption), color="red")
        plt.title("One day power consumption")
        plt.xlabel("seconds")
        plt.ylabel("Power [W]")
        plt.show()
