import unittest
from collections import deque


# https://www.interviewcake.com/question/python/inflight-entertainment?section=hashing-and-hash-tables&course=fc1
# Use deque

# Time = O(n)
# Space = O(n)

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Determine if two movie runtimes add up to the flight length
    # And do not show the same movie twice.

    lengths = deque(movie_lengths)

    while len(lengths) > 0:
        current_length = lengths.popleft()
        second_length = flight_length - current_length
        if second_length in lengths:
            return True

    return False


# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)