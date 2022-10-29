import unittest
from energy_system import meter
import matplotlib.pyplot as plt


class TestMeter(unittest.TestCase):
    def test_meter_general(self):
        # imput vals are positive from 0 till 86400
        hours = []
        simulated_power_consumption = meter.simulate_day_power_consumption(min_consumption=0,
                                                                                          max_consumption=9000)

        plt.rcParams["figure.autolayout"] = True
        plt.plot(*zip(*simulated_power_consumption), color="red")
        plt.title("One day power consumption")
        plt.xlabel("seconds")
        plt.ylabel("Power [W]")
        plt.show()