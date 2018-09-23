import unittest


# https://www.interviewcake.com/question/python/queue-two-stacks?course=fc1&section=queues-stacks
# Implement a queue from two stacks.

# Time: O(m), where m is the number of enqueue and dequeue operations.


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        # It is always ok to append to the in_stack.
        # Even if items have already been moved to out_stack,
        # additional items will not be taken from in_stack until
        # out_stack is emptied.
        self.in_stack.append(item)

    def dequeue(self):

        # If out_stack is empty, then replenish it.
        if len(self.out_stack) == 0:

            # Pop each item off the in_stack and
            # append it to the out_stack.
            while len(self.in_stack) > 0:
                latest_item = self.in_stack.pop()
                self.out_stack.append(latest_item)

            # If after copying all elements from the in stack, the out_stack
            # is still empty, then throw IndexError
            if len(self.out_stack) == 0:
                raise IndexError('Cannot dequeue from an empty queue.')

        return self.out_stack.pop()


# Tests

class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)