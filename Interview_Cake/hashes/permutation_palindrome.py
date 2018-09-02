import unittest


# https://www.interviewcake.com/question/python/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
# Use set to keep track of characters with an odd count
# O(n) because we iterate over the list one time.


def has_palindrome_permutation(the_string):
    # Check if any permutation of the input is a palindrome

    odd_set = set()

    for character in the_string:
        if character in odd_set:
            odd_set.remove(character)
        else:
            odd_set.add(character)

    if len(odd_set) <= 1:
        return True
    else:
        return False


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)