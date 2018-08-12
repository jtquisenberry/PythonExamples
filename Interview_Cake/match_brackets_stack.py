import unittest
# https://www.interviewcake.com/question/python/bracket-validator?section=queues-stacks&course=fc1

def is_valid(code):
    # Determine if the input code is valid

    if len(code) == 0:
        return True

    couples = {'}': '{', ']': '[', ')': '('}
    brackets_stack = []

    # iterate over code
    for character in code:
        if character not in couples:
            # opening paren
            brackets_stack.append(character)

        elif len(brackets_stack) == 0:
            # Closing bracket first means mismatch
            return False

        elif brackets_stack[-1] == couples[character]:
            # Found a match, remove the opening paren
            # from the stack.
            brackets_stack.pop()

        else:
            # add to stack
            # closing with mismatch
            # short-circuit the rest of the tests.
            return False

    if len(brackets_stack) == 0:
        return True
    else:
        return False


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)