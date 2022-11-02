import unittest
from pv_simulator import solar_pannel
import matplotlib.pyplot as plt


class TestSolarPanel(unittest.TestCase):
    def test_get_power_general(self):
        # imput vals are positive from 0 till 86400
        pv_values = []
        seconds = []
        hours = []
        for sec in range(0, 86400, 1):
            val = solar_pannel.get_solar_power(sec)
            # print(f"hour: {round((sec/60/60),2)} sec: {sec} : {val}")
            pv_values.append(val)
            seconds.append(sec)
            hours.append(round((sec/60/60), 2))

        plt.rcParams["figure.autolayout"] = True
        plt.plot(hours, pv_values, color="red")
        plt.title("Solar panel day characteristic")
        plt.xlabel("hours")
        plt.ylabel("Power [W]")
        plt.show()

    def test_get_power_type(self):
        with self.assertRaises(Exception) as context:
            solar_pannel.get_solar_power(0.12123)
        self.assertTrue('TypeError' in str(context.exception))

    def test_get_power_lower_bound(self):
        # imput vals are positive from 0 till 86400
        self.assertEqual(0, solar_pannel.get_solar_power(0))

    def test_get_power_upper_bound(self):
        # imput vals are positive from 0 till 86400
        self.assertEqual(0, solar_pannel.get_solar_power(86400))

    def test_get_power_negative_val(self):
        # imput vals are positive from 0 till 86400
        with self.assertRaises(Exception) as context:
            solar_pannel.get_solar_power(-1)
        self.assertTrue('ValueError' in str(context.exception))

    def test_get_power_too_big_val(self):
        # imput vals are positive from 0 till 86400
        with self.assertRaises(Exception) as context:
            solar_pannel.get_solar_power(86401)
        self.assertTrue('ValueError' in str(context.exception))

