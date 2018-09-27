import unittest

# https://www.interviewcake.com/question/python/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
# Use set to keep track of characters with an odd count
# O(n) because we iterate over the list one time.

# Our approach is to check that each character appears an even number of times,
# allowing for only one character to appear an odd number of times (a middle character).
# This is enough to determine if a permutation of the input string is a palindrome.
# We iterate through each character in the input string, keeping track of the characters we've seen
# an odd number of times using a set unpaired_characters.
# As we iterate through the characters in the input string:
# If the character is not in unpaired_characters, we add it.
# If the character is already in unpaired_characters, we remove it.
# Finally, we just need to check if less than two characters don’t have a pair.

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