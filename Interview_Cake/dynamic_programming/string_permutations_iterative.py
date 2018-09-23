import unittest


# https://www.interviewcake.com/question/python/recursive-string-permutations?section=dynamic-programming-recursion&course=fc1
# Get all permutations of a string.
# Iterative version


def get_permutations(string):
    # Generate all permutations of the input string

    if len(string) < 1:
        return set([string])

    permutations_temp = set()
    permutations_temp.add(string[0])
    permutations = set()
    permutations.add(string[0])

    for char in string[1:]:
        permutations = set()
        for permutation in permutations_temp:

            for i in range(len(permutations_temp) + 1):
                start = permutation[:i]
                end = permutation[i:]
                out = start + char + end
                permutations.add(out)

            permutations_temp = permutations

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