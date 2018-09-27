import unittest


# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space-beast-mode?course=fc1&section=trees-graphs
# Find a number that appears more than once ... in O(n) time
# Time: O(n)
# Space: O(1)

# A. We know the position of a node with multiple incoming pointers is a duplicate in our list because the nodes that pointed to it must have the same value.
# B. We find a node with multiple incoming pointers by finding the first node in a cycle.
# C. We find the first node in a cycle by finding the length of the cycle and advancing two pointers: one starting at the head of the linked list, and the other starting ahead as many steps as there are nodes in the cycle. The pointers will meet at the first node in the cycle.
# D. We find the length of a cycle by remembering a position inside the cycle and counting the number of steps it takes to get back to that position.
# E. We get inside a cycle by starting at the head and walking nn steps. We know the head of the list is at position n + 1.

def find_duplicate(int_list):
    # Find a number that appears more than once ... in O(n) time

    # n is the head of the list.
    n = len(int_list) - 1

    # JQ
    # For this problem, "position" is defined as index + 1
    # *** We are using position, rather than index because the first integer is 1 ***.
    # If the first integer were zero, we could use index.

    # STEP 1: GET INSIDE A CYCLE
    # Start at position n+1 and walk n steps to
    # find a position guaranteed to be in a cycle
    # if there are four items in the list, then n is
    # This position is guaranteed to be within a cycle
    # because the latest a cycle can occur is at the tail.

    # position = head index + 1
    position = n + 1
    for _ in range(n):
        position = int_list[position - 1]

    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # Find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    # Find the length of the cycle
    remembered_position = position
    # Advance position by one to accommodate the while loop
    position = int_list[position - 1]
    length_of_cycle = 1

    while remembered_position != position:
        position = int_list[position - 1]
        length_of_cycle += 1

    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # Start two pointers
    #   (1) at position n+1
    #   (2) ahead of position n+1 as many steps as the cycle's length
    # Create a stick with a length equal to the size of the cycle.
    start_position = n + 1
    advance_position = n + 1

    for _ in range(length_of_cycle):
        advance_position = int_list[advance_position - 1]

    # Advance both positions until they are at the same position
    # Advance until the pointers are in the same position
    # which is the first node in the cycle
    while start_position != advance_position:
        start_position = int_list[start_position - 1]
        advance_position = int_list[advance_position - 1]

    # Since there are multiple values pointing to the first node
    # in the cycle, its position is a duplicate in our list
    return start_position


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)