import unittest
import re

# https://www.interviewcake.com/question/python/word-cloud?course=fc1&section=hashing-and-hash-tables
# This module is only inspired by an Interview Cake problem.
# The actual problem does not recommend the use of regular expressions.

def split_words(sentence):

    if 'mushroom' in sentence:
        raise ValueError('No mushroom allowed')

    # This does not split on hyphens or apostrophes
    # apostrophe would have to be written as \'
    words = re.split(r'[,"?!.: ]', sentence)

    # conversion to lowercase
    # removal of empty words
    words = [word.lower() for word in words if word > '']
    words.sort()
    return words


class Test(unittest.TestCase):

    def setUp(self):
        self.dogs = 'dogs'

    def test_mushroom(self):
        with self.assertRaises(ValueError):
            sentence = 'I like mushrooms'
            actual = split_words(sentence)

    def test_word1(self):
        sentence = 'Chocolate cake for dinner and pound cake for dessert'
        expected = ['and', 'cake', 'cake', 'chocolate', 'dessert', 'dinner', 'for', 'for', 'pound']
        actual = split_words(sentence)
        self.assertEqual(expected, actual)

    def test_word2(self):
        sentence = 'Mmm...mmm...decisions...decisions'
        expected = ['decisions', 'decisions', 'mmm', 'mmm']
        actual = split_words(sentence)
        #print(actual)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
