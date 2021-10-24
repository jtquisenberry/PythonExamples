import unittest
import pytest

# In order to win the prize for most cookies sold, my friend Alice and I are
# going to merge our Girl Scout Cookies orders and enter as one unit.

# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in lists.
# Write a function to merge our lists of orders into one sorted list.

# For example:

# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print(merge_lists(my_list, alices_list))

# ------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# Where n is the number of items in the merged list.
# ---------------------------------------------------

def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list

    if my_list == []:
        return alices_list

    if alices_list == []:
        return my_list

    my_list_index = 0
    alices_list_index = 0

    merged_list = []

    while my_list_index < len(my_list) and alices_list_index < len(alices_list):

        if my_list[my_list_index] < alices_list[alices_list_index]:
            merged_list.append(my_list[my_list_index])
            my_list_index += 1

        elif alices_list[alices_list_index] < my_list[my_list_index]:
            merged_list.append(alices_list[alices_list_index])
            alices_list_index += 1

    while my_list_index < len(my_list):
        merged_list.append(my_list[my_list_index])
        my_list_index += 1

    while alices_list_index < len(alices_list):
        merged_list.append(alices_list[alices_list_index])
        alices_list_index += 1

    return merged_list


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)