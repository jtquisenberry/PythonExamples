import unittest
import pytest

# Your company delivers breakfast via autonomous quadcopter drones. And something mysterious
# has happened.

# Each breakfast delivery is assigned a unique ID, a positive integer. When one of the
# company's 100 drones takes off with a delivery, the delivery's ID is added to a list,
# delivery_id_confirmations. When the drone comes back and lands, the ID is again added
# to the same list.

# After breakfast this morning there were only 99 drones on the tarmac. One of the
# drones never made it back from a delivery. We suspect a secret agent from Amazon placed an
# order and stole one of our patented drones. To track them down, we need to find their delivery ID.

# Given the list of IDs, which contains many duplicate integers and one unique integer,
# find the unique integer.

# The IDs are not guaranteed to be sorted or sequential. Orders aren't always fulfilled in the
# order they were received, and some deliveries get cancelled before takeoff.

import unittest


def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list

    return 0


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
