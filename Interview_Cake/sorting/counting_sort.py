import unittest


# https://www.interviewcake.com/question/python/top-scores?course=fc1&section=sorting-searching-logarithms
# Sort in descending order
# Counting Sort with list
# Sort the scores in O(n) time
# The for loop forces the scores to sort in order, in this case descending order.


def sort_scores(unsorted_scores, highest_possible_score):
    # Sort the scores in O(n) time

    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score + 1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []

    # for score in range(len(score_counts)):
    # range is start (inclusive), end (exclusive), step
    for score in range(len(score_counts) - 1, -1, -1):
        # print(score)
        count = score_counts[score]

        # excludes zero counts

        for time in range(count):
            sorted_scores.append(score)

        # This also works.
        # sorted_scores += [score] * count

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

if __name__ == '__main__':
    unittest.main(verbosity=2)