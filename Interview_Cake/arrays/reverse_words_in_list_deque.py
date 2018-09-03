import unittest
from collections import deque


# https://www.interviewcake.com/question/python/reverse-words?section=array-and-string-manipulation&course=fc1
# Solution with deque

def reverse_words(message):
    if len(message) < 1:
        return message

    final_message = deque()
    current_word = []

    for i in range(0, len(message)):
        character = message[i]

        if character != ' ':
            current_word.append(character)

        if character == ' ' or i == len(message) - 1:

            # Use reversed otherwise extend puts characters in the wrong order.
            final_message.extendleft(reversed(current_word))
            current_word = []
            if i != len(message) - 1:
                final_message.extendleft(' ')

    for i in range(0, len(message)):
        message[i] = list(final_message)[i]

    return list(final_message)


# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)