import unittest
from collections import deque


def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    my_queue = deque(my_list)
    alices_queue = deque(alices_list)

    merged_list = []

    while len(my_queue) > 0 and len(alices_queue) > 0:
        if (my_queue[0] < alices_queue[0]):
            merged_list.append(my_queue[0])
            my_queue.popleft()
        else:
            merged_list.append(alices_queue[0])
            alices_queue.popleft()

    if len(my_queue) > 0:
        merged_list.extend(my_queue)
    if len(alices_queue) > 0:
        merged_list.extend(alices_queue)

    return merged_list


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)