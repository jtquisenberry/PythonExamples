import unittest


# https://www.interviewcake.com/question/python/find-in-ordered-set?course=fc1&section=combinatorics-probability-math

# Determine whether an integer is present in a sorted list.
# Use a binary search.
# Time: O(lg n) because using binary search.
# Space: O(1)


def contains(ordered_list, number):
    # Check if an integer is present in the list

    if len(ordered_list) < 1:
        return False

    floor = 0
    ceiling = len(ordered_list) - 1

    # The last iteration should occur when floor and ceiling are two apart.
    # If we check whether they are one apart, floor division will always keep them apart.
    while floor + 1 < ceiling:
        # midpoint is calculated on the basis of indexes.
        midpoint = floor + (ceiling - floor) // 2

        # Check whether the number is the in the left half or the right half.
        if number <= ordered_list[midpoint]:
            ceiling = midpoint
        else:
            floor = midpoint

    # The floor and ceiling have converged. If it is in the list, it must be
    # at index floor or index ceiling.
    if number in [ordered_list[floor], ordered_list[ceiling]]:
        return True

    return False


# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)