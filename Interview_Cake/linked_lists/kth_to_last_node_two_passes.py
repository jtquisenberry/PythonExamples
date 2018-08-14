import unittest
# https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list?course=fc1&section=linked-lists
# Time = O(n), the time required to traverse the list
#      Note that this should be slower than one pass, but time complexity can be deceiving because
#      O(2n) simplifies to O(n) after disregarding the constant.
# Space = O(1), the memory required to current_node, list_length, and current_position

def kth_to_last_node(k, head):
    # Return the kth to last node in the linked list
    current_node = head
    list_length = 0
    while current_node:
        # print(current_node.value)
        list_length += 1
        current_node = current_node.next
    # print(list_length)

    # print(list_length) - k + 1

    if k > list_length:
        raise ValueError('k is greater than the length of the linked list')
    if k == 0:
        raise ValueError('k must be greater than zero.')

    current_node = head
    current_position = 1
    while current_position < list_length - k + 1:
        current_position += 1
        current_node = current_node.next

    # print(current_node.value)
    return current_node


# Tests

class Test(unittest.TestCase):
    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)