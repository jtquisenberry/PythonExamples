import unittest


# https://www.interviewcake.com/question/python/largest-stack?section=queues-stacks&course=fc1

# O(1) time for push(), pop(), and get_max(). O(m)
# additional space, where m is the number of operations performed on the stack.

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    # Implement the push, pop, and get_max methods

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):

        # Note the >= . This allows the addition of an item if it is identical
        # to the previous maximum. The can be duplicate maxima.
        if item >= self.maxes_stack.peek() or self.maxes_stack.peek() is None:
            self.maxes_stack.push(item)

        self.stack.push(item)

    def pop(self):

        item = self.stack.pop()

        # If the current item is the maximum, then it should be removed
        # from the stack of maxima. Since that maximum is the last element,
        # a simple pop suffices.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):

        return self.maxes_stack.peek()


# Tests

class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)