import unittest


# alphabetical rotation point
# https://www.interviewcake.com/question/python/find-rotation-point?course=fc1&section=sorting-searching-logarithms


def find_rotation_point(words):
    # Find the rotation point in the list

    if len(words) < 2:
        raise IndexError('At least two words are required')

    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:

        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        # If guess comes after the first word or is the first word,
        # then we are still in a sequence starting with the
        # first word and continuing through the current word.
        # The rotation point (alphabetically first word) must appear later.
        # Must use >= in case floor index = guess index, as in 0 = (1-0//2)
        if words[guess_index] > first_word:

            # Look to the right by advancing floor_index to guess
            floor_index = guess_index

        else:
            # current word appears after the rotation point.
            # Look to the left by bringing ceiling to guess.
            ceiling_index = guess_index

        if floor_index + 1 == ceiling_index:

            if words[-1] > words[0]:
                return 0

            else:

                return ceiling_index


# Tests
class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    def test_sorted_list(self):
        actual = find_rotation_point(['a', 'b', 'c', 'd', 'e'])
        expected = 0
        self.assertEqual(actual, expected)

    def test_rotation_at_end(self):
        actual = find_rotation_point(['u', 'v', 'w', 'x', 'a'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_too_small_list(self):
        with self.assertRaises(IndexError):
            find_rotation_point(['a'])

    # Are we missing any edge cases?


if __name__ == '__main__':
    unittest.main(verbosity=2)