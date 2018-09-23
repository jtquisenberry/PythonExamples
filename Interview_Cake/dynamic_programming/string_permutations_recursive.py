import unittest


# https://www.interviewcake.com/question/python/recursive-string-permutations?section=dynamic-programming-recursion&course=fc1
# Get all permutations of a string.
# Recursive version

# This is a top-down approach. We start with the full string and reduce it to smaller segments
# string, string[:-1], string[:-2], ...  ,string[0]
# The base case is the first character.

# We need two variables to store permutations permutations_temp stores the results of the
# previous round of recursion.
# permutations is reset each round and contains the permutations constructed this round.


def get_permutations(string):
    # Generate all permutations of the input string

    # Base case
    if len(string) <= 1:
        return set([string])

    string_minus_last = string[:-1]
    last = string[-1]

    permutations = set()
    permutations_temp = get_permutations(string_minus_last)

    for permutation in permutations_temp:
        for i in range(len(permutation) + 1):
            start = permutation[:i]
            end = permutation[i:]
            combined = start + last + end
            permutations.add(combined)

    return permutations


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)