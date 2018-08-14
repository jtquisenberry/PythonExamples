import unittest
# https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list?course=fc1&section=linked-lists
# Time = O(n), the time required to traverse the list
#      Note that this should be faster than two passes, but time complexity can be deceiving because
#      O(2n) simplifies to O(n) after disregarding the constant.
# Space = O(n), the memory required to store the dictionary.

def kth_to_last_node(k, head):
    # Return the kth to last node in the linked list

    nodes_dictionary = dict()

    current_node = head
    length_of_list = 0

    while current_node:
        length_of_list += 1
        nodes_dictionary[length_of_list] = current_node
        current_node = current_node.next

    if k == 0:
        raise ValueError('k == 0')
    if k > length_of_list:
        raise ValueError('k is too big')

    requested_position = length_of_list - k + 1

    return nodes_dictionary[requested_position]


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