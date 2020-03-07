import unittest


# https://www.interviewcake.com/question/python/find-unique-int-among-duplicates?section=bit-manipulation&course=fc1

# Given a list containing pairs of numbers and a single unique number,
# identify the unique number.
# Matching numbers can be cancelled by adding or removing from a set.
# Time O(n) look at each item once. Average case lookup time for set is O(1)
# Space: O(n) In the worst case, unique_ids contains n//2 + 1 before cancelling begins.


def find_unique_delivery_id(delivery_ids):
    # Find the one unique ID in the list

    unique_ids = set()

    for delivery_id in delivery_ids:
        if delivery_id in unique_ids:
            unique_ids.remove(delivery_id)
        else:
            unique_ids.add(delivery_id)

    # print(list(unique_ids))
    return (list(unique_ids)[0])


# Tests

class Test(unittest.TestCase):

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)