import unittest

# Determine whether a linked list contains a cycle.

# https://www.interviewcake.com/question/python/linked-list-cycles?course=fc1&section=linked-lists

# This solution could resulting traversing all nodes two times.
# Even though this is O(n), it is only because O(2n) simplifies to
# O(n) after disregarding the constant.
# Space complexity = O(1)


def contains_cycle(first_node):
    # Check if the linked list contains a cycle

    fast_runner = first_node
    slow_runner = first_node

    while fast_runner is not None and fast_runner.next is not None:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next
        if fast_runner == slow_runner:
            return True

    return False


# Tests

class Test(unittest.TestCase):
    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def test_linked_list_with_no_cycle(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_cycle_loops_to_beginning(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fourth.next = first
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_cycle_loops_to_middle(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = third
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_two_node_cyle_at_end(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = fourth
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_empty_list(self):
        result = contains_cycle(None)
        self.assertFalse(result)

    def test_one_element_linked_list_no_cycle(self):
        first = Test.LinkedListNode(1)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_one_element_linked_list_cycle(self):
        first = Test.LinkedListNode(1)
        first.next = first
        result = contains_cycle(first)
        self.assertTrue(result)


unittest.main(verbosity=2)