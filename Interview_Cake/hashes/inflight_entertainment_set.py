import unittest


# https://www.interviewcake.com/question/python/inflight-entertainment?section=hashing-and-hash-tables&course=fc1

# Time = O(n)
# Space = O(n)

# We make one pass through movie_lengths, treating each item as the first_movie_length. At each iteration, we:
# 1. See if there's a matching_second_movie_length we've seen already (stored in our movie_lengths_seen set)
# that is equal to flight_length - first_movie_length. If there is, we short-circuit and return True.
# 2. Keep our movie_lengths_seen set up to date by throwing in the current first_movie_length.
# We know users won't watch the same movie twice because we check movie_lengths_seen for matching_second_movie_length
# before we've put first_movie_length in it!

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Determine if two movie runtimes add up to the flight length
    # And do not show the same movie twice.

    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

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