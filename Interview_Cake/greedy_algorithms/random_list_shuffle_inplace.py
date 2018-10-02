import random
import unittest


# from datetime import datetime

# https://www.interviewcake.com/question/python/shuffle?section=greedy&course=fc1
# Random in place shuffle
# *******  # Swap each element for a random element AFTER it.  ************
# Fisher-Yates shuffle
# Time = O(n)
# Space = O(1)


# Avoid a non-uniform distribution. We do not want to swap each element
# in the list with any 'ol element in the list. It must be swaped with
# a later element.


# Suppose our list had 3 elements: [a, b, c]. This means it'll make 3 calls
# to get_random(0, 2). That's 3 random choices, each with 3 possibilities.
# So our total number of possible sets of choices is 3*3*3 = 27. Each of these
# 27 sets of choices is equally probable. The problem is that there are only
# six possible outcomes 3! = 6. Since 27 is not divisible by 6, the possibilities
# are not equally likely and not uniform.


def get_random(floor, ceiling, seed):
    random.seed(seed)
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list, seed):
    # Shuffle the input in place

    # Swap each element for a random element AFTER it.
    # Earlier elements have already been randomized. Disturbing
    # them will result in a non-uniform distribution,
    for first_index in range(len(the_list)):
        # Swap first_index with a later (or current) second index
        second_index = get_random(first_index, len(the_list) - 1, seed)

        # Do the swap
        the_list[first_index], the_list[second_index] = the_list[second_index], the_list[first_index]


class TestCase(unittest.TestCase):

    def setUp(self):
        self.seed = 3

    def testA(self):
        expected = [2, 3, 1, 4, 5]
        actual = [1, 2, 3, 4, 5]
        shuffle(actual, self.seed)
        # print('actual', actual)
        self.assertEqual(expected, actual)

    def testB(self):
        expected = [4, 5, 1, 2, 3]
        actual = [1, 2, 3, 4, 5]
        shuffle(actual, 99)
        # print('actual', actual)
        self.assertEqual(expected, actual)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
