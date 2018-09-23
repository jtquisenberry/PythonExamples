import unittest


# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space?course=fc1&section=sorting-searching-logarithms
# Time: O(n * lg n)
# Space: O(1)

# 1. Find the number of integers in our input list which lie within the range 1..n/2.
# 2. Compare that to the number of possible unique integers in the same range.
# 3. If the number of actual integers is greater than the number of possible integers, we know there is a duplicate in the range 1..n/2, so we iteratively use the same approach on that range.
# 4. #If the number of actual #integers is not greater than the number of possible integers, we know there must be duplicate in the range n/2 + 1..n, so we iteratively use the same approach on that range.
# 5. At some point, our range will contain just 1 integer, which will be our answer.

def find_repeat(the_list):
    # The integers are in the range 1..n1
    # The list has a length of n+1
    # Find a number that appears more than once

    # Notice that this is not "floor_index" and "ceiling_index"
    # We are not dividing the list by index but by values.
    # That is also why floor = 1
    floor = 1
    ceiling = len(the_list) - 1

    # The answer is known when floor and ceiling converge.
    while floor < ceiling:

        midpoint = floor + ((ceiling - floor) // 2)

        # Specify two ranges of numbers (not indexes),
        # a lower range and an upper range.
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        # print("lower range", lower_range_floor, lower_range_ceiling)
        # print("upper range", upper_range_floor, upper_range_ceiling)

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        # print("items_in_lower_range", items_in_lower_range)

        distinct_possible_integers_in_lower_range = (
                lower_range_ceiling
                - lower_range_floor
                + 1
        )

        # print("distinct_possible_integers_in_lower_range", distinct_possible_integers_in_lower_range)

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            # Converge on the lower range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            # Converge on the upper range.
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    # print("floor", floor)
    # print("ceiling", ceiling)
    return floor


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)