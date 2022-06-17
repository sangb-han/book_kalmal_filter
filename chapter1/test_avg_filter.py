import unittest

import random
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

from chapter1.avg_filter import AverageFilter


def get_volt() -> float:
    w = 4 * (random.random() - 0.5)
    return 14.4 + w


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.avg_filter = AverageFilter()

    def test_average(self):

        samples = np.arange(0, 10, 0.2)

        avg_saved = np.full_like(samples, 0)
        v_saved = np.full_like(samples, 0)

        i = 0
        for s in samples:
            v = get_volt()
            average = self.avg_filter.average(v)

            avg_saved[i] = average
            v_saved[i] = v

            i = i+1

        plt.plot(samples, v_saved, label='Measured', marker='x', color='r')
        plt.plot(samples, avg_saved, label='Average', marker='o', color='c')
        plt.legend()
        plt.show()
        self.assertEqual(samples.size, 50)  # add assertion here

if __name__ == '__main__':
    unittest.main()
