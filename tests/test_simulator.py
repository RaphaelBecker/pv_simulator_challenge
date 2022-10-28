import unittest
from meter import simulator
import matplotlib.pyplot as plt


class TestSum(unittest.TestCase):
    def test_get_power(self):
        # imput vals are positive from 0 till 86400
        pv_values = []
        seconds = []
        for sec in range(0, 86400, 10):
            val = simulator.get_power(sec)
            print(f"hour: {round((sec/60/60),2)} sec: {sec} : {val}")
            pv_values.append(val)
            seconds.append(sec)

        plt.rcParams["figure.autolayout"] = True
        plt.plot(seconds, pv_values, color="red")
        plt.show()
