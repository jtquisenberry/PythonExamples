################################
# Problem
################################

# I have a list of n+1 numbers. Every number in the range 1..n appears once except
# for one number that appears twice.

#Write a function for finding the number that appears twice.


import unittest
import pytest


def find_repeat(numbers_list):

    # Find the number that appears twice

    sum_using_triangular_series = ((len(numbers_list)-1) ** 2 + (len(numbers_list)-1)) / 2
    sum_using_sum = sum(numbers_list)
    duplicated_number = sum_using_sum - sum_using_triangular_series

    return duplicated_number


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)