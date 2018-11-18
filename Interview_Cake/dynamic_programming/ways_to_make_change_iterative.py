import unittest


# https://www.interviewcake.com/question/python/coin?section=dynamic-programming-recursion&course=fc1
# Iterative method
# Time O(n*m): n = amount, m = number of denominations.
# Space O(n):

# Must have coins on the outer loop, otherwise will do duplicate counting.
# The result is the non-distinct number of ways (permutations).
# We are looking for the distinct number of ways.

# Amounts in outer loop
       #3$                            [3]                [3,1]
       #2$                  [2]       [2,1]              [2,1,1], [2,2]
       #1$   [0]    [1]     [1,1]     [1,1,1], [1,2]     [1,1,1,1], [1,1,2], [1,2,1], [1,3]
# Amounts    0      1       2             3                 4

# Coins in outer loop
      #3$                                            [3,1]
      #2$                   [2]        [2,1]         [2,1,1], [2,2]
      #1$    [0]    [1]     [1,1]      [1,1,1]       [1,1,1,1]
# Amounts    0      1       2             3                 4

# It may help to think of the amounts in outer loop problem as trees, which is how recursion would work.
# At value = 3 and denominations 1,2,3
#
#              1           2        3
#          1   2  3      1   2     2
#         1 2   1       1
#        1
#
# The 1,1,2 and 1,2,1, and 2,1,1 trees are redundant.


def change_possibilities(amount, denominations):
    # Calculate the number of ways to make change

    # This list contains one index for each possible amount up to amount
    # The + 1 is necessary to ensure there is an index for amount.
    ways_of_calculating_interim_amounts = [0] * (amount + 1)

    # There is one way makeing amount 0
    # We need this base case so that we add one if the interim_capacity is zero.
    ways_of_calculating_interim_amounts[0] = 1

    # For each coin
    for coin in denominations:

        # for each interim amount.
        # Include +1 to make a range inclusive of the total amount.
        for interim_amount in range(amount + 1):

            # Check whether coin fits into the interim amount.
            # Could be simplified to for interim_amount in range(coin, amount +1)
            if coin <= interim_amount:
                # There is a way to make the total amount. That way is
                # current coin plus the ways needed to make a lesser amount
                # that excludes the coin.
                # The case where the lesser amount is 0 is why we have the base case
                # ways[0] = 1
                ways_of_calculating_interim_amounts[interim_amount] += (

                    # It is not 1 + the smaller value.
                    # Suppose that coin 5 fits in amount 6.
                    # If there are only coins (2 and 5), it does not matter that
                    # 5 fits in 6 because there are no ways to make 1.
                    # Index 1 should have a value of 0.
                    ways_of_calculating_interim_amounts[interim_amount - coin]

                )

    # Return the value at the final amount
    return ways_of_calculating_interim_amounts[-1]


# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = change_possibilities(5, (2, 3))
        expected = 1
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)