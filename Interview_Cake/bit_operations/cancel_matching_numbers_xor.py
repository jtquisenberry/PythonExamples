import unittest


# https://www.interviewcake.com/question/python/find-unique-int-among-duplicates?section=bit-manipulation&course=fc1

# Given a list containing pairs of numbers and a single unique number,
# identify the unique number.
# Matching numbers can be cancelled with XOR, which is ^
# Time O(n) look at each item once.
# Space: O(1) allocating unique_delivery_id


def find_unique_delivery_id(delivery_ids):
    # Find the one unique ID in the list

    if len(delivery_ids) < 1:
        raise ValueError('At least one value is required.')

    # Initialize to 0 because x ^ 0 = x
    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id


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

if __name__ == '__main__':
    unittest.main(verbosity=2)