import unittest

# --------------------------
# Problem
# --------------------------

# Write a function that takes a list of characters and reverses the letters in place.

# Why a list of characters instead of a string?

# The goal of this question is to practice manipulating strings in place. Since we're modifying the input,
# we need a mutable type like a list, instead of Python 2.7's immutable strings.

# --------------------------

# https://www.interviewcake.com/question/python/reverse-string-in-place?section=array-and-string-manipulation&course=fc1
# space = O(1)
# time = O(n) - walking through the list of characters one time.

# Reverse the order of a string in place.
# We swap the first and last characters, then the second and second-to-last characters,
# and so on until we reach the middle.

# Use a while loop to converge on the center of the list.



def reverse(list_of_chars):

    # Reverse the input list of chars in place


    pass


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)