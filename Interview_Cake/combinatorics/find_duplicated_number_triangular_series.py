import unittest


# https://www.interviewcake.com/question/python/which-appears-twice?course=fc1&section=combinatorics-probability-math
# Find the number that appears twice in a list.
# There is a list of n + 1 numbers, and every number in the range 1..n appears once, except that
# one number is duplicated.
# Recognize that this is triangular series.

# Space O(1)
# Time O(n)

# 1. Sum all numbers 1..n using (n ** 2 + n) / 2.
# 2. Sum all numbers in input list using sum(numbers_list)
# 3. The difference between the two sums is the extra number.


def find_repeat(numbers_list):
    # Find the number that appears twice

    # Get sum of 1..n. Recall that n is one less than the length of the list.
    # Interview Cake method
    sum_of_1_n = (((len(numbers_list) - 1) ** 2) + len(numbers_list) - 1) / 2
    # Alternative method = (first + last) * number_of_pairs
    # numbers_list.sort()
    # sum_of_1_n = int((numbers_list[0] + numbers_list[-1]) * (len(numbers_list) / float(2)))

    # Get sum of numbers in list
    sum_of_numbers = sum(numbers_list)

    # Find the difference.
    output = sum_of_numbers - sum_of_1_n

    return output


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


unittest.main(verbosity=2)