from unittest import TestCase

from chapter1.mov_avg_filter import MovAverageFilter

import numpy as np

class TestMovAverageFilter(TestCase):


    def setUp(self) -> None:
        self.avg_filter = MovAverageFilter(10)

    def test_average(self):
        self.fail()
