import unittest


# https://www.interviewcake.com/question/python/which-appears-twice?course=fc1&section=combinatorics-probability-math
# Find the number that appears twice in a list.
# This version is not the recommended version. This version uses a set.

# Space O(n)
# Time O(n)


def find_repeat(numbers_list):
    # Find the number that appears twice
    number_set = set()

    for number in numbers_list:
        if number in number_set:
            return number
        else:
            number_set.add(number)

    return


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