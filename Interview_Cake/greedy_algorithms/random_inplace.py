import random
import unittest
from datetime import datetime


# https://www.interviewcake.com/question/python/shuffle?section=greedy&course=fc1
# Random in place shuffle
# Fisher-Yates shuffle
# Time = O(n)
# Space = O(1)


def get_random(floor, ceiling, seed):
    random.seed(seed)
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list, seed):
    # Shuffle the input in place

    for index_to_populate in range(len(the_list)):
        index_to_swap_with = get_random(index_to_populate, len(the_list) - 1, seed)
        the_list[index_to_populate], the_list[index_to_swap_with] = the_list[index_to_swap_with], the_list[
            index_to_populate]


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

    def teadDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
