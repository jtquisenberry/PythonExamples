import unittest


# https://www.interviewcake.com/question/python/matching-parens?section=queues-stacks&course=fc1

# With a counter

# Time: O(n) - traverse string once.
# Space O(1) - Storing only the count of open parens.


def get_closing_paren(sentence, opening_paren_index):
    # Find the position of the matching closing parenthesis

    open_parens = 0

    for position in range(opening_paren_index, len(sentence)):
        if sentence[position] == '(':
            open_parens += 1

        elif sentence[position] == ')':
            open_parens -= 1
            if open_parens == 0:
                return position

    if open_parens > 0:
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


if __name__ == '__main__':
    unittest.main(verbosity=2)