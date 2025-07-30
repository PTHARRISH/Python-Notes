import os
import sys

sys.path.append(os.path.abspath(".."))
from geek_for_geeks.challenge.move_zero import pushZerosToEnd
from geek_for_geeks.challenge.reverse_an_array import reverseArray
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


class TestPushZerosToEnd:
    def test_general_case(self):
        arr = [1, 0, 2, 0, 4, 0, 5]
        expected = [1, 2, 4, 5, 0, 0, 0]
        pushZerosToEnd(arr)
        assert arr == expected

    def test_all_zeros(self):
        arr = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        pushZerosToEnd(arr)
        assert arr == expected

    def test_no_zeros(self):
        arr = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        pushZerosToEnd(arr)
        assert arr == expected

    def test_empty_list(self):
        arr = []
        expected = []
        pushZerosToEnd(arr)
        assert arr == expected

    def test_single_element_zero(self):
        arr = [0]
        expected = [0]
        pushZerosToEnd(arr)
        assert arr == expected

    def test_single_element_nonzero(self):
        arr = [5]
        expected = [5]
        pushZerosToEnd(arr)
        assert arr == expected

    def test_mixed_types(self):
        arr = [0, 1, 0, 0, 2, 0, 3]
        expected = [1, 2, 3, 0, 0, 0, 0]
        pushZerosToEnd(arr)
        assert arr == expected


class TestReverseArray:
    def test_even_length(self):
        arr = [1, 2, 3, 4]
        expected = [4, 3, 2, 1]
        assert reverseArray(arr) == expected

    def test_odd_length(self):
        arr = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        assert reverseArray(arr) == expected

    def test_single_element(self):
        arr = [7]
        expected = [7]
        assert reverseArray(arr) == expected

    def test_empty_list(self):
        arr = []
        expected = []
        assert reverseArray(arr) == expected

    def test_palindrome_list(self):
        arr = [1, 2, 3, 2, 1]
        expected = [1, 2, 3, 2, 1]
        assert reverseArray(arr) == expected


U
