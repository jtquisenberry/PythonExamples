import unittest
import pytest

# alphabetical rotation point
# https://www.interviewcake.com/question/python/find-rotation-point?course=fc1&section=sorting-searching-logarithms

# I want to learn some big words so people think I'm smart.

# I opened up a dictionary to a page in the middle and started flipping through,
# looking for words I didn't know. I put each word I didn't know at increasing indices in a
# huge list I created in memory. When I reached the end of the dictionary, I started from
# the beginning and did the same thing until I reached the page I started at.

# Now I have a list of words that are mostly alphabetical, except they start somewhere in the
# middle of the alphabet, reach the end, and then start from the beginning of the alphabet.
# In other words, this is an alphabetically ordered list that has been "rotated." For example:

#  words = [
#    'ptolemaic',
#    'retrograde',
#    'supplant',
#    'undulate',
#    'xenoepist',
#    'asymptote',  # <-- rotates here!
#    'babka',
#    'banoffee',
#    'engender',
#    'karpatka',
#    'othellolagkage',
# ]

# Write a function for finding the index of the "rotation point," which is where I started working
# from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so
# we want to be efficient here.

# To keep things simple, you can assume all words are lowercase.

# Gotchas
# We can get O(lg{n}) time.


def find_rotation_point(words):
    # Find the rotation point in the list
    pass


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