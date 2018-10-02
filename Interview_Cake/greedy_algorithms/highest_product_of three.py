# https://www.interviewcake.com/question/python/highest-product-of-3?course=fc1&section=greedy
# Calculate the highest product of three numbers
# Time = O(n)
# Space = O(n) (because using a slice)
# Space = O(1) if using indexes instead.

# For a greedy problem, the idea is to keep track of the best solution
# so far and the variables needed to calculate a better solution if one arises.
# Setup often involves setting initial values to the first elements in a list.
# In this case setting initial values of 0 would not work because the for loop
# will not iterate over indexes 0 or 1, and their values would be ignored.

# STEPS
# Set initial values equal to early elements in the list.
# For each later element, do comparison to determine the current case
# is the best case.
# Update the precursors.


import unittest


def highest_product_of_3(list_of_ints):
    # Calculate the highest product of three numbers

    if len(list_of_ints) < 3:
        raise ValueError('Three values are required')

    # Since the for loop below is starting at index 2,
    # The highest and lowest of the previous two elements must be calculated.
    # Otherwise, they will be ignored.
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Remembering this slice is critical
    for number in list_of_ints[2:]:
        highest_product_of_3 = max(highest_product_of_3, number * highest_product_of_2, number * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2, number * highest, number * lowest)
        lowest_product_of_2 = min(lowest_product_of_2, number * highest, number * lowest)

        highest = max(highest, number)
        lowest = min(lowest, number)

    return highest_product_of_3


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)