import unittest


# https://www.interviewcake.com/question/python/matching-parens?section=queues-stacks&course=fc1

# With a stack

# Time: O(n) - traverse string once.
# Space O(n) - possibly storing all characters


def get_closing_paren(sentence, opening_paren_index):
    # Find the position of the matching closing parenthesis

    paren_stack = list()

    for position in range(opening_paren_index, len(sentence)):
        if sentence[position] == '(':
            paren_stack.append('(')

        elif sentence[position] == ')':
            paren_stack.pop()
            if len(paren_stack) == 0:
                return position

    if len(paren_stack) > 0:
        raise Exception("Exception")


# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


if __name__ == '__name__':
    unittest.main(verbosity=2)