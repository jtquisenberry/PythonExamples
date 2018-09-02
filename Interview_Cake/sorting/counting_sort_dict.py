import unittest


# https://www.interviewcake.com/question/python/top-scores?course=fc1&section=sorting-searching-logarithms
# Sort in descending order
# Counting Sort with dictionary
# Sort the scores in O(n) time


def sort_scores(unsorted_scores, highest_possible_score):
    # Sort the scores in O(n) time

    # List of 0s at indices 0..highest_possible_score
    score_counts = {}

    # Populate score_counts
    for score in unsorted_scores:
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1

    sorted_scores = []

    # Counting is what imposes a sort order.
    # The keys() might not be sorted.
    for score in range(highest_possible_score, -1, -1):
        if score in score_counts:
            sorted_scores += [score] * score_counts[score]

    return sorted_scores


# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)