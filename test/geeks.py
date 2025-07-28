import os
import sys

sys.path.append(os.path.abspath(".."))
from geek_for_geeks.challenge.secondlargest import getSecondLargest


class Test_getSecondLargest:
    def test_basic(self):
        assert getSecondLargest([2, 3, 6, 6, 5]) == 5

    def test_all_same(self):
        assert getSecondLargest([4, 4, 4]) == -1

    def test_one_element(self):
        assert getSecondLargest([10]) == -1

    def test_negative_numbers(self):
        assert getSecondLargest([-5, -2, -9, -1]) == -2

    def test_empty_array(self):
        assert getSecondLargest([]) == -1
